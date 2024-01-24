from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, timedelta
import copy


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/blk'
db = SQLAlchemy(app)

class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Integer)
	method = db.Column(db.Integer, db.ForeignKey('method.id'), nullable=True)
	who = db.Column(db.String)
	desc = db.Column(db.String)
	cat = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
	amount = db.Column(db.Float)

	category = db.relationship("Category", back_populates="transactions")
	method_obj = db.relationship("Method", back_populates="transactions")

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	parent_id = db.Column(db.Integer)
	name = db.Column(db.String(100))
	color = db.Column(db.Integer)

	transactions = db.relationship("Transaction", back_populates="category")

class Method(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))

	transactions = db.relationship("Transaction", back_populates="method_obj")

@app.route('/transactions', methods=['GET', 'POST', 'DELETE'])
def manage_transactions():
	if request.method == 'POST':
		data = request.json
		entry = Transaction(
			date = data['date'],
			method = data['method'],
			who = data['who'],
			desc = data['desc'],
			cat = data['cat'],
			amount = data['amount']
		)
		db.session.add(entry)
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
	elif request.method == 'DELETE':
		data = request.json
		transaction_id = data['id']
		obj = Transaction.query.get(transaction_id)
		db.session.delete(obj)
		db.session.commit()
		return jsonify({"message": "Delete successful"}), 200
	else:
		entries = Transaction.query.all()
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

@app.route('/categories', methods=['GET', 'POST'])
def manage_categories():
	if request.method == 'POST':
		data = request.json
		entry = Category(
			parent_id = data['cat'],
			name = data['who'],
			color = data['amount']
		)
		db.session.add(entry)
		db.session.commit()
		return jsonify(
			{
				'id': entry.id,
				'name': entry.name,
				'parent_id': entry.parent_id,
				'color': entry.color
			}
		)
	else:
		entries = Category.query.all()
		return jsonify([
			{
				'id': entry.id,
				'name': entry.name,
				'parent_id': entry.parent_id,
				'color': entry.color
			} for entry in entries
		])

@app.route('/methods', methods=['GET', 'POST'])
def manage_methods():
	if request.method == 'POST':
		data = request.json
		entry = Method(
			name = data['who']
		)
		db.session.add(entry)
		db.session.commit()
		return jsonify(
			{
				'id': entry.id,
				'name': entry.name,
			}
		)
	else:
		entries = Method.query.all()
		return jsonify([
			{
				'id': entry.id,
				'name': entry.name,
			} for entry in entries
		])
if __name__ == '__main__':
	db.create_all()  # Create database tables
	app.run(debug=True, host='192.168.0.101')


	