import requests
import json
import uuid
import hashlib
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

def SendBook(DATA,fileip):
    headers = {'Content-Type': 'application/json'}
    d = requests.post(fileip+"/book",headers=headers,data= json.dumps(DATA))
    return d.text
def SendCancel(DATA,fileip):
    headers = {'Content-Type': 'application/json'}
    can=requests.post(fileip+"/cancel",headers=headers,data= json.dumps(DATA))
    return can.text

def GetList(fileip):
    r= requests.get(fileip+"/list")
    return r.text

def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()
    
def check_password(hashed_password, user_password):
    password= hashed_password
    return password == hashlib.sha256(user_password.encode()).hexdigest()
 
# new_pass = input('Please enter a password: ')
# hashed_password = hash_password(new_pass)
# print('The string to store in the db is: ' + hashed_password)


def SendLogin(User,hashed_Pass,fileip):
    headers = {'Content-Type': 'application/json'}
    da={"Username":User,"Password":hashed_Pass}
    b= requests.post(fileip+"/login",headers=headers,data= json.dumps(da) )
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


def SendRegister(User,hashed_Pass,fileip):
    headers = {'Content-Type': 'application/json'}
    da={"Username":User,"Password":hashed_Pass}
    b= requests.post(fileip+"/regis",headers=headers,data= json.dumps(da) )
    k = b.text
    return k

A=getipfromfile("config.txt")