import json

def Login(input):
    data = json.loads(input)
    if(data["Username"]):
        return json.dumps({"status":"success","cookie_session":"/////","admin":"yes"})
    else :
        return json.dumps({"status":"fail","cookie_session":"////","admin":"no"})
        
    
    
