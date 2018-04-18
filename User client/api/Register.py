import requests
import json
def getipfromfile(file):
    fileip = ""
    l1 = []
    d1 = ""
    file_object  = open(file, "r")

    for line in file_object:
        l1=line.split("=")
        d1=l1[1].split("\n")
        fileip = str(fileip)+d1[0]
    return fileip

def SendRegister(User,hashed_Pass,fileip):
    headers = {'Content-Type': 'application/json'}
    da={"Username":User,"Password":hashed_Pass}
    b= requests.post(fileip+"/regis",headers=headers,data= json.dumps(da) )
    k = b.text
    return k

def check(username,password):
        print(len(password))
        if(len(password) > 5):
            if(len(password) < 15):
                if(len(username) > 5):
                    if(len(username) < 15):
                        return 1
        return 0
    
A=getipfromfile("config.txt")

##Sendlogin("Muchshu",hash_password("Muchshu"),A)
