de = {  "room":"309/1",
        "data":"lab room",
        "schedule":{
            {'date':'6275',
            'user':'sdsdsd'},
            {'date':'6255',
            'user':'555555'},
            {'date':'6275',
            'user':'354'},
            {'date':'6275',
            'user':'555555'}
        },
        "room":"400",
        "data":"lab room",
        "schedule":[
            {'date':'11111',
            'user':'aaaa'},
            {'date':'bbbb',
            'user':'555555'},
            {'date':'ccccc',
            'user':'354'},
            {'date':'eeeee',
            'user':'555555'}
        ]
        
        }

def Test(d):
    stripKeys=["schedule",'user']
    jsonTemp1 = d
    jsonTemp2 = {}
    for key in stripKeys :
        print(jsonTemp1[key])
        jsonTemp2 = jsonTemp1[key]
        if jsonTemp2:
            jsonTemp1[key] = jsonTemp2
    if jsonTemp2:
        return jsonTemp2
    return None

# print(Test(de))

def findkeys(node, kv):
	if isinstance(node, list):
		for i in node:
			for x in findkeys(i, kv):
				yield x
	elif isinstance(node, dict):
		if kv in node:
			yield node[kv]
		for j in node.values():
			for x in findkeys(j, kv):
				yield x
#room_db = list(findkeys(DB.get_room(), "room"))
#date_db = list(findkeys(DB.get_room(), "Data_Time"))

def Jprint(JSON):
  print(json.dumps(JSON,sort_keys=True,indent=2))


# s =next(d for d in de['schedule'] if d['date']=='627f') 
# if s == None:
#     print('MOOOO')