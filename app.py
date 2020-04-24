#set FLASK_APP=flaskr
#set FLASK_ENV=development
#flask run
#
###############
#gcloud app deploy
#


from flask import Flask, request
from flask_cors import CORS
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
import json
from bson.objectid import ObjectId

application = app = Flask(__name__)
cors = CORS(app)
DB_NAME = "pydb"  
DB_HOST = "ds159025.mlab.com"
DB_PORT = 59025
DB_USER = "pydatabase" 
DB_PASS = "pythondatabase123"


connection = MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

#collection = db.customers

#post = {
#		"name": "Johnny",
#		"address": "Highway 3"
#	   }

@app.route("/")
def hello():
    return "Welcome to Python Flask!"
	
@app.route("/getPesticides", methods = ['GET'])
def getPesticides():
    pesticides = db.pesticides.find()
    return dumps(pesticides)
	
@app.route('/pesticides/<pesticideid>', methods = ['GET'])
def api_medicine(pesticideid):
    pesticideIdOne = db.pesticides.find_one({'_id': ObjectId(pesticideid)})
    return dumps(pesticideIdOne)	

@app.route('/postUser', methods=['POST'])
def add_user():
  user = db.users
  #print(request.data)
  data = json.loads(request.data)
  print(data)
  user_id = user.insert_one(data)
  #new_user = user.find_one({'_id': user_id })
  #output = {'name' : new_user['name'], 'email' : new_user['email'], 'password' : new_user['password']}
  #return dumps(output)
  return "Succesfully added"

@app.route('/users/<useremail>', methods = ['GET'])
def api_user(useremail):
    userOne = db.users.find_one({'email': useremail})
    return dumps(userOne)
  
if __name__ == "__main__":
    app.run(debug=True)