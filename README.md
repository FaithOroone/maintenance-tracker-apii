# Maintenance-Tracker-API



## Description
This API allows users to create maintenance or repair requests to operations/repairs department and monitor the status of their respective requests, 28/06/2018
### Required Features(Endpoints)
Endpoint                         Functionality 
* POST/api/v1/auth/signup	Register a user
* POST/api/v1/auth/login	login a user
* POST /api/v1/users/requests/	Create a request
* GET /api/v1/users/requests	Fetch all the requests of a logged in user
* GET /api/v1/users/arequest	Fetch a request that belongs to a logged in user
* PUT /api/v1/users/arequest	Modify a request.

### Prerequisites
Python/Flask framework
### Setup/Installation Requirements
Install Python
Install pip
Setup a virtual environment
pip install Flask
pip install pytest
Run App
Run python app.py on command prompt
View the api on http://127.0.0.1:5000/api/v1/users/requests
Test it's usage with postman
### License
Copyright (c) 2018
