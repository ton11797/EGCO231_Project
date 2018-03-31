#import
from pymongo import MongoClient

#Hello word

# ////////////////////////////////////////////////////////
# load config


# ///////////////////////////////////////////////////////
# log


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
	def get_room(self):
		return self.
	def login(self,username,password):
		self.user = self.db['userData']
		if str(self.username)==str(self.user.f) and str(self.password)==str(self.db['password']):
			return True
		else :
			return False
DB = database()
print(DB.have_user("admin"))
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


# ///////////////////////////////////////////////////////