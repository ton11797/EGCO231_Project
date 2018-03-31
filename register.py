import json

def Register(input):
    data = json.loads(input)
    if(have_user(data["Username"]):
        return json.dumps('{"status":"fail","error":"This username is already in use"')
    else:
        if(len(data["Password"])<17 and len(data["Password"])>7):
            insert(json.dumps("{\"Username\":"+data["Username"]+",\"Password\":"+data["Password"]))
            return json.dumps('{"status":"success","error":"none"')
        else:
            return json.dumps('{"status":"fail","error":"your password must contain between 8 and 15 letters and numbers"')
     

