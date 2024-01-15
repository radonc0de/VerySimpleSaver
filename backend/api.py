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
	method = db.Column(db.Integer)
	who = db.Column(db.String)
	desc = db.Column(db.String)
	cat = db.Column(db.String)
	amount = db.Column(db.Float)

@app.route('/transactions', methods=['GET', 'POST'])
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

if __name__ == '__main__':
	db.create_all()  # Create database tables
	app.run(debug=True)


	