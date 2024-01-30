from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta
import jwt
import datetime
import hashlib
import os
from waitress import serve


app = Flask(__name__)
CORS(app)
db_url = os.environ["DB_URL"]
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(100))
	createdAt = db.Column(db.Integer)

	transactions = db.relationship("Transaction", back_populates="user")
	methods = db.relationship("Method", back_populates="user")
	categories = db.relationship("Category", back_populates="user")

class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Integer)
	method = db.Column(db.Integer, db.ForeignKey('method.id'), nullable=True)
	who = db.Column(db.String)
	desc = db.Column(db.String)
	cat = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
	amount = db.Column(db.Float)
	user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	user = db.relationship("Account", back_populates="transactions")
	category = db.relationship("Category", back_populates="transactions")
	method_obj = db.relationship("Method", back_populates="transactions")

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	parent_id = db.Column(db.Integer)
	name = db.Column(db.String(100))
	color = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	user = db.relationship("Account", back_populates="categories")
	transactions = db.relationship("Transaction", back_populates="category")

class Method(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	user = db.relationship("Account", back_populates="methods")
	transactions = db.relationship("Transaction", back_populates="method_obj")

secret_key = 'move_me_somewhere'
salt = 'me_too'

def get_by_email(email):
	try:
		user = Account.query.filter_by(email=email).first()
		if user:
			return user 
		else:
			return None
	except:
		return None

def create_jwt(email):
	payload = {
		'email' : email,
		'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)
	}
	token = jwt.encode(payload, secret_key, algorithm='HS256')
	return token

def decode_jwt(token):
	try:
		decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
		return decoded_payload['email']
	except jwt.ExpiredSignatureError:
		return None
	except jwt.InvalidTokenError:
		return None
	return 

def salt_and_hash_pass(password):
	password_salt = (password + salt).encode()
	hashed_password = hashlib.sha256(password_salt).hexdigest()
	return hashed_password

def authenticate(request):
	header_value = request.headers.get('token')
	email = decode_jwt(header_value)
	if header_value and email:
		#return None
		return get_by_email(email) 
	else:
		return None

@app.route('/login', methods=['POST'])
def login_request():
	if request.method == 'POST':
		data = request.json
		user = get_by_email(data['email'])
		hashed_password = salt_and_hash_pass(data['password'])
		if user and user.password == hashed_password:
			token = create_jwt(user.email)
			print('returning token: ' + token)
			return jsonify({"token": token})
		else:
			return jsonify({"message": "Invalid Credentials"}), 401

@app.route('/createaccount', methods=['POST'])
def create_account():
	if request.method == 'POST':
		data = request.json
		entry = Account(
			email = data['email'],
			password = salt_and_hash_pass(data['password']),
			createdAt = int(datetime.datetime.utcnow().timestamp())
		)
		db.session.add(entry)
		db.session.commit()
		return jsonify({"message": "Account created successfully"}), 200
		
@app.route('/transactions', methods=['GET', 'POST', 'DELETE', 'PUT'])
def manage_transactions():

	user = authenticate(request)
	if user == None:
		return jsonify({"message": "Unauthorized"}), 401 

	if request.method == 'GET':
		entries = Transaction.query.filter_by(user_id=user.id).all()
		return jsonify([
			{
				'id': entry.id,
				'date' : entry.date,
				'method' : entry.method,
				'who' : entry.who,
				'desc' : entry.desc,
				'cat' : entry.cat,
				'amount' : entry.amount
			} for entry in entries
		])
		
	data = request.json

	if request.method == 'DELETE':
		transaction_id = data['id']
		entry = Transaction.query.get(transaction_id)

		entry.session.delete(obj)
		entry.session.commit()
		return jsonify({"message": "Delete successful"}), 200

	if request.method == 'POST':
		entry = Transaction(
			date = data['date'],
			method = data['method'],
			who = data['who'],
			desc = data['desc'],
			cat = data['cat'],
			amount = data['amount'],
			user_id = user.id
		)
		db.session.add(entry)

	elif request.method == 'PUT':
		transaction_id = data['id']
		entry = Transaction.query.get(transaction_id)

		entry.date = data['date']
		entry.method = data['method']
		entry.who = data['who']
		entry.desc = data['desc']
		entry.cat = data['cat']
		entry.amount = data['amount']

	# for put and post
	db.session.commit()
	return jsonify(
		{
			'id': entry.id,
			'date' : entry.date,
			'method' : entry.method,
			'who' : entry.who,
			'desc' : entry.desc,
			'cat' : entry.cat,
			'amount' : entry.amount
		}
	)

@app.route('/categories', methods=['GET', 'POST', 'PUT'])
def manage_categories():
	user = authenticate(request)
	if user == None:
		return jsonify({"message": "Unauthorized"}), 401 

	if request.method == 'GET':
		entries = Category.query.filter_by(user_id=user.id).all()
		return jsonify([
			{
				'id': entry.id,
				'name': entry.name,
				'parent_id': entry.parent_id,
				'color': entry.color
			} for entry in entries
		])
	
	data = request.json
	
	if request.method == 'POST':
		entry = Category(
			parent_id = data['parent_id'],
			name = data['name'],
			color = data['color'],
			user_id = user.id
		)
		db.session.add(entry)

	elif request.method == 'PUT':
		cat_id = data['id']
		entry = Category.query.get(cat_id)

		entry.parent_id = data['parent_id']
		entry.name = data['name']
		entry.color = data['color']

	db.session.commit()
	return jsonify(
		{
			'id': entry.id,
			'name': entry.name,
			'parent_id': entry.parent_id,
			'color': entry.color
		}
	)


@app.route('/methods', methods=['GET', 'POST', 'PUT'])
def manage_methods():
	user = authenticate(request)
	if user == None:
		return jsonify({"message": "Unauthorized"}), 401 

	if request.method == 'GET':
		entries = Method.query.filter_by(user_id=user.id).all()
		return jsonify([
			{
				'id': entry.id,
				'name': entry.name,
			} for entry in entries
		])

	data = request.json

	if request.method == 'POST':
		entry = Method(
			name = data['name'],
			user_id = user.id
		)
		db.session.add(entry)

	elif request.method == 'PUT':
		mth_id = data['id']
		entry = Method.query.get(mth_id)
		entry.name = data['name']

	db.session.commit()
	return jsonify(
		{
			'id': entry.id,
			'name': entry.name,
		}
	)

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify(
        {
            'message' : 'Amazing! Amazing! This is just like magic!' 
        }
    )

if __name__ == '__main__':
	with app.app_context():
		db.create_all()  # Create database tables
	serve(app, host="0.0.0.0", port=5000)



