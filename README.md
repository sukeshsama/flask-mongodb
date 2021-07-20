# Python Flask based API to save user input to MongoDB

## Requirements:
1. CentOs or any other linux flavor
2. Python 3.6 +
3. Install MongoDB Instructions are here -> https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/ 
4. Recommend to setup Virtual Environment to install tools for running this code -> python3 -m venv /path/to/new/virtual/environment
5. Move to /path/to/new/virtual/environment and run source bin/activate and install flask and Flask-PyMongo using PIP
6. Download code from Git and navigate to /flask-mongodb/src folder and run python app.py
7. From Browser http://127.0.0.1:5000/form and input your message and enter
8. To validate the data run this from browser http://127.0.0.1:5000/read

## What else can be done to run this setup automatically:
1. Build Docker Image with an entry point to start app.py automatically
2. Run Docker Image in any multi cloud or on bare metal using ansible


