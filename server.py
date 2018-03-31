#import
from pymongo import MongoClient
import random
import string
import json

from flask import Flask, url_for,Response,request,json

# ////////////////////////////////////////////////////////
# load config


# ///////////////////////////////////////////////////////
# log
def printdata(data):
    file = open("log.txt","a")
    print(data,end="")
    file.write(data)
    file.close
# ///////////////////////////////////////////////////////
# database
class database:
	def __init__(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client['EGCO']
	def have_user(self,username):
		self.user = self.db['userData']
		if str(self.user.find_one({"username":username})) == "None":
			return False
		else:
			return True

	def register(self,username,password):
		if self.have_user(username):
			respond = {"status":"Fail","error":"username exist"}
			return json.dumps(respond)
		else:
			self.user.insert_one({"username":username,"password":password})
			respond = {"status":"sucess","error":"username exist"}
			return json.dumps(respond)

	def rand_string(self,length, char_set=10):
		output = ''
		for _ in range(length): output += random.choice(char_set)
		return output

	def get_room(self):
		self.room = self.db['room']
		collect = self.room.find({})
		array =[]
		for c in collect:
			del c['_id']
			array.append(c)
		respond = {"available-room":array}
		return json.dumps(respond)

	def genCookies(self,username):
		self.session = self.db['loginSession ']
		self.random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
		self.session.insert_one({"username":username,"cookies":self.random})
		return self.random

	def login(self,username,password):
		self.user = self.db['userData']
		if self.user.find_one({"username":username,"password":password})=="None":
			respond = {"status":"Fail","error":"username or password not match"}
			return json.dumps(respond)
		else:
			self.cookies = self.genCookies(username)
			self.admin = "no"
			if username=="admin":
				self.admin = "yes"
			respond = {"status":"sucess","error":"none","cookie_session":self.cookies,"admin":self.admin}
			return json.dumps(respond)



DB = database()
# print(DB.have_user("admin"))
# print(DB.get_room())
print(DB.login("admin","123"))
printdata("test\n")
printdata("test\n")
printdata("test\n")
printdata("test\n")
printdata("test\n")

# ///////////////////////////////////////////////////////
# book


# ///////////////////////////////////////////////////////
# login


# ///////////////////////////////////////////////////////
# cancel


# ///////////////////////////////////////////////////////
# register


# ///////////////////////////////////////////////////////
# get room


# ///////////////////////////////////////////////////////
# Route

app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def api_login():
    if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
			return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_LOGIN"

@app.route('/regis', methods = ['POST'])
def api_regis():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
			return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_REGIS"

@app.route('/book', methods = ['POST'])
def api_book():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
				return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_BOOK"

@app.route('/cancel', methods = ['POST'])
def api_cancel():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
				return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_CANCEL"
@app.route('/list', methods = ['GET'])
def api_list():
	if request.method =='GET': return "list of Room"
	else: return "fail_POST_CANCEL"
if __name__ == '__main__':
	app.run()

# ///////////////////////////////////////////////////////
