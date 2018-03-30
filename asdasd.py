from pymongo import MongoClient
import datetime
import pprint
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection

import json
json_data = json.load(open('m.json'))
#print(json.dumps(json_data,sort_keys=True,indent=2))

test = [
        {'usserData':{}},
        {'room':json_data},
        {'loginSession':{}}
        ]
posts = db.posts
posts.remove()
result = posts.insert_many(test)
result.inserted_ids
#pprint.pprint(posts.find_one({"_id": post2_id}))
for post in posts.find():
    pprint.pprint(post)

posts.find({'usserData':{}})






from bson.objectid import ObjectId
# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
