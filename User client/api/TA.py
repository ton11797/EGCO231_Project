import requests
import json
import uuid
import hashlib




s1 = ""
l1 = []
d1 = ""

file_object  = open("config.txt", "r")

for line in file_object:
    l1=line.split("=")
    print(l1[1].split("\n"))
    d1=l1[1].split("\n")
    s1 = str(s1)+d1[0]






def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


while(1):
    new_pass = input('Please enter a password: ')
    if (len(new_pass) > 5 & len(new_pass) < 15):
            print("shittttttttttt")
            break


hashed_password = hash_password(new_pass)







Much="///////////////////////////////"
da={"Username":"Much","Password":"Muchshu1"}
headers = {'Content-Type': 'application/json'}
print("///////////////////////////////")
r= requests.get(s1+"/list")
print(r.text)
print("///////////////////////////////")






c= requests.post(s1+"/regis",headers=headers,data=json.dumps(da))
print(c.text)
print("///////////////////////////////")
b= requests.post(s1+"/login",headers=headers,data= json.dumps(da) )
k = b.text
print(k)
##print("///////////////////////////////") 
##daa=json.loads(r.text)
##print(daa["available-room"])
cookie=json.loads(b.text)
print("///////////////////////////////")
print(cookie["cookie_session"])
COOKIE=cookie["cookie_session"]
print("///////////////////////////////")
databook={
  "Data":[
    { 
      "Room":"6272",
      "Data_Time":"4/2/61 08:00-11:00"
    },
    { 
      "Room":"6272",
      "Data_Time":"4/2/61 10:00-11:00"
    },
    { 
      "Room":"meeting room",
      "Data_Time":"4/2/61 10:00-11:00"
    },
    { 
      "Room":"6272",
      "Data_Time":"5/2/61 11:00-13:00"
    }
    
  ],
  "cookie_session":COOKIE
}
d = requests.post(s1+"/book",headers=headers,data= json.dumps(databook))
print(d.text)
print("///////////////////////////////")
can=requests.post(s1+"/cancel",headers=headers,data= json.dumps(databook))
print(can.text)

