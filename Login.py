import json

input = json.load(open('egco231_putlogin.json'))
def Login(input):
    data = json.loads(input)
    if(login(data["Username"],data["Password"])):
        return json.dumps({"status":"success","cookie_session":"/////","admin":"yes"})
    else :
        return json.dumps({"status":"fail","cookie_session":"////","admin":"no"})
        
    
    
