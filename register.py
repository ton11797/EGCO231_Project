import json

input = json.load(open('egco231_putlogin.json'))
def Register(input):
    data = json.loads(input)
    if(have_user(data["Username"]):
        return json.dumps('{"status":"fail","error":"This username is already in use"')
    else:
        insert(json.dumps("{\"Username\":"+data["Username"]+",\"Password\":"+data["Password"]))
        return json.dumps('{"status":"success","error":"none"')

