from flask import Flask, request, jsonify
from .models import users, users
import re

app = Flask(__name__)
@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
	user_data = request.get_json()
	if not user_data:
		return jsonify({'message':'please fill in all the fields '}),400

	first_name = str(user_data.get('first_name'))
	last_name = str(user_data.get('last_name'))
	email = user_data.get('email')
	password = user_data.get('password')
	confirm_password = user_data.get('confirm_password')

	if not first_name or first_name == type(int) or first_name == " ":
		return jsonify({'message':'a vaild First_name is required'}), 400

	if not last_name or last_name == type(int) or last_name == " ":
		return jsonify({'message':'a valid Last_name is required'}), 400

	if not email or email == " ":
		return jsonify({'message':'email is required'}), 400

	if not password or password == " " or len(password)< 8 or re.search("[a-z]",password):
		return jsonify({'message':'password is required'}), 400

	if not confirm_password or password == " " or len(password)< 8:
		return jsonify({'message':'please confirm your password is required'}), 400

	users.append(user_data)
	return jsonify({"message":"you have successfully signed in."}),201

@app.route('/api/v1/auth/login', methods=['POST'])
def logIn():
	user_data = request.get_json()
	email=user_data.get('email')
	password=user_data.get('password')
	if not email or email == " ":
		return jsonify({'message':'email is required'}), 400
	if not password or password == " " or len(password)< 8:
		return jsonify({'message':'password is required'}), 400
	users.append(user_data)
	return jsonify({"message":"you have successfully logged in."}),201

