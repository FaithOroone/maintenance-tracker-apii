from flask import Flask, request, jsonify
from .models import users, users, Requests, requests
import re

app = Flask(__name__)
@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
	user_data = request.get_json()
	if not user_data:
		return jsonify({'message':'please fill in all the fields '}),400

	first_name = str(user_data.get('first_name'))
	last_name = str(user_data.get('last_name'))
	user_id =int(user_data.get('user_id'))
	email = user_data.get('email')
	password = user_data.get('password')
	confirm_password = user_data.get('confirm_password')

	if not first_name or first_name == type(int) or first_name == " ":
		return jsonify({'message':'a vaild First_name is required'}), 400

	if not last_name or last_name == type(int) or last_name == " ":
		return jsonify({'message':'a valid Last_name is required'}), 400

	if not user_id or user_id == type(str) or user_id == " ":
		return jsonify({'message':'a valid user_id is required'}), 400

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
	user_id = user_data.get('user_id')
	email=user_data.get('email')
	password=user_data.get('password')

	if not user_id or user_id == type(str) or user_id == " ":
		return jsonify({'message':'a valid user_id is required'}), 400
	if not email or email == " ":
		return jsonify({'message':'email is required'}), 400
	if not password or password == " " or len(password)< 8:
		return jsonify({'message':'password is required'}), 400
	users.append(user_data)
	return jsonify({"message":"you have successfully logged in."}),201

@app.route('/api/v1/users/request', methods=['POST'])
def create_request():
	request_data = request.get_json()
	if not request_data:
		return jsonify({'message':'please fill in all the fields to login '}),400

	name = request_data.get('name')
	category = request_data.get('category')
	request_type = request_data.get('request_type')
	description = request_data.get('description')
	department = request_data.get('department')
	request_id = request_data.get('request_id')
	status = request_data.get('status')

	if not name or name == type(int) or name == " ":
		return jsonify({'message':'name is required'}), 400
	if not category:
		return jsonify({'message':'category is required'}), 400
	if not request_type:
		return jsonify({'message':'request_type is required'}), 400
	if not description or  description == type(int) or  description ==" ":
		return jsonify({'message':'description is required'}), 400
	if not department:
		return jsonify({'message':'department is required'}), 400
	if not request_id or request_id == "" or request_id == type(str):
		return jsonify({'message':'request_id is required'}), 400
	if not status:
		return jsonify({'message':'status is required'}), 400

	requests.append(request_data)
	return jsonify({"message":"we have recieved your request. Thank you"}),201


@app.route("/api/v1/user/requests", methods=["GET"])
def fetch_requests():
    if len(requests)>0:
        return jsonify({"message":"you have successfully fetched requests"}), 302
    else:
        return jsonify({"message":"There are no requests found"}), 400

@app.route("/api/v1/user/requests/<int:_id>", methods=["GET"])
def fetch_arequest(request_id):
    for arequest in requests:
        if arequest.get['request_id']==requests:
            return jsonify({'requests': arequest})
        else:
            return jsonify({'message':'request not found'}), 400

@app.route("/api/v1/user/requests/<int:request_id>", methods=["PUT"])
def modify_arequest(request_id):
    if len(requests)<1:
        return jsonify({"message":"you have no request to modify"}), 400
    if len(requests) >= 1:
        request_data = request.get_json()
        name = request_data.get('name')
        category = request_data.get('category')
        request_type = request_data.get('request_type')
        description =request_data.get("description")
        department =request_data.get('department')
	request_id =request_data.get('request_id')
	status = request_data.get("status")

        for arequest in requests:
            if arequest.request_id == int(request_id):
                arequest.name == name
                arequest.category == category
                arequest.request_type == request_type
                arequest.description == description
                arequest.department == department
                arequest.status == status
            return jsonify({"message":"your request has been modified"}), 201





