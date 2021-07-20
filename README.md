# Python Flask based API to save the user input to MongoDB

## Requirements:
1. CentOs or any other linux flavor
2. Python 3.6 +
3. Docker installed, incase if app needs to run inside container
4. Install MongoDB, follow Instructions from here -> https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/ 

## Run Flask locally

1. Recommend to setup Virtual Environment to install tools for running this code  
   $python3 -m venv /path/to/new/virtual/environment
2. Move to /path/to/new/virtual/environment and run source bin/activate and install flask and Flask-PyMongo using PIP
3. Download code from Git and navigate to /flask-mongodb/src folder and run python app.py
4. From Browser http://127.0.0.1:5000/form and input your message and enter
5. To validate the data run this from browser http://127.0.0.1:5000/read

## Build Docker Image and Run Flask in a container
Clone code from Git[https://github.com/sukeshsama/flask-mongodb.git] and navigate to /flask-mongoder folder and run docker build commands

$docker build -t python-flask:latest  
$docker run -d --network=host -p 5000:5000 python-flask:latest  

From Browser Go to http://127.0.0.1:5000/form and input your message and enter. this will save Data to MongoDB Collection.  
To validate the data in MongoDB run this from browser http://127.0.0.1:5000/read

## What else can be done to run this setup automatically:
1. Run Docker Image in any multi cloud or on bare metal using ansible or any other deployment tools



