# Python Flask based API to save the user input to MongoDB

## Requirements:
1. CentOs or any other linux flavor
2. Python 3.6 +
3. Docker intalled incase if app needs to run inside container
4. Install MongoDB Instructions are here -> https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/ 
5. Recommend to setup Virtual Environment to install tools for running this code -> python3 -m venv /path/to/new/virtual/environment
6. Move to /path/to/new/virtual/environment and run source bin/activate and install flask and Flask-PyMongo using PIP
7. Download code from Git and navigate to /flask-mongodb/src folder and run python app.py
8. From Browser http://127.0.0.1:5000/form and input your message and enter
9. To validate the data run this from browser http://127.0.0.1:5000/read

## Build Docker Image and Run Flask in a container
$docker build -t python-flask:latest  
$docker run -d --network=host -p 5000:5000 python-flask:latest  

From Browser http://127.0.0.1:5000/form and input your message and enter
To validate the data run this from browser http://127.0.0.1:5000/read

## What else can be done to run this setup automatically:
2. Run Docker Image in any multi cloud or on bare metal using ansible


