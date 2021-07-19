import datetime

from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#connect and create a db named as mydb
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mydb"

#initializing the client for mongodb
mongo = PyMongo(app)

#creating collection
message_collection = mongo.db.messages

@app.route("/form")
def form():
   return render_template('form.html')

@app.route("/data", methods=['GET'])
def show_data():
    if request.method == 'GET':
        message = request.args.get("msg")
        timestamp = datetime.datetime.now()
        if message != "":
            message = message_collection.insert_one({"message": message, "timeadded": timestamp})
            return ("Data added to the database")
        else:
            return ("No data provided")

@app.route("/read")
def read_data():
    message = (message_collection.find())
    return render_template('index.html', message = message)

@app.route("/delete")
def delete():
    message_collection.remove({})
    return "All data deleted"

if __name__ == '__main__':
    app.run(debug=True)
