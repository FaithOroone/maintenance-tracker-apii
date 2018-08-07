from flask import Flask, request, jsonify, make_response
from .models import Request, requests

app = Flask(__name__)
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

@app.route("/api/v1/user/requests/<int:request_id>", methods=["GET"])
def fetch_arequest(request_id):
    for arequest in requests:
        if arequest.get['id']==requests:
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



