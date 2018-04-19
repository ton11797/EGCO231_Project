import requests
import json
import uuid
import hashlib
class API_cen():
    def __init__(self):
        self.config = self.getipfromfile("config.txt")
        self.username = ""
        self.cookies = ""
        self.admin = False
    def getipfromfile(self,file):
        fileip = ""
        l1 = []
        d1 = ""
        file_object  = open(file, "r")

        for line in file_object:
            l1=line.split("=")
            d1=l1[1].split("\n")
            fileip = str(fileip)+d1[0]
        return fileip

    def SendBook(self,DATA):
        headers = {'Content-Type': 'application/json'}
        DATA['cookie_session']=self.cookies
        d = requests.post(self.config+"/book",headers=headers,data= json.dumps(DATA))
        return d.text
    def SendCancel(self,DATA):
        headers = {'Content-Type': 'application/json'}
        DATA['cookie_session']=self.cookies
        can=requests.post(self.config+"/cancel",headers=headers,data= json.dumps(DATA))
        return can.text

    def GetList(self):
        r= requests.get(self.config+"/list")
        return r.text

    def hash_password(self,password):

        return hashlib.sha256(password.encode()).hexdigest()
        
    def check_password(self,hashed_password, user_password):
        password= hashed_password
        return password == hashlib.sha256(user_password.encode()).hexdigest()
    
    # new_pass = input('Please enter a password: ')
    # hashed_password = hash_password(new_pass)
    # print('The string to store in the db is: ' + hashed_password)


    def SendLogin(self,User,Pass):
        headers = {'Content-Type': 'application/json'}
        da={"Username":User,"Password":self.hash_password(Pass)}
        b= requests.post(self.config+"/login",headers=headers,data= json.dumps(da) )
        k = b.text
        if json.loads(k)['status']== "Fail" :
            return k
        self.cookies = json.loads(k)['cookie_session']
        self.username = User
        return k 

    def check(self,username,password):
            print(len(password))
            if(len(password) > 5):
                if(len(password) < 15):
                    if(len(username) > 5):
                        if(len(username) < 15):
                            return 1
            return 0
    def SendRegister(self,User,Pass):
        headers = {'Content-Type': 'application/json'}
        da={"Username":User,"Password":self.hash_password(Pass)}
        b= requests.post(self.config+"/regis",headers=headers,data= json.dumps(da) )
        k = b.text
        return k
    
    def get_user(self):
        return self.username
A = API_cen()
# data ={
#     "Data":[
#       { 
#         "room":"6275",
#         "date":"2/2/61",
#         "time":"08:00-11:00"
#       },
#       { 
#         "room":"6275",
#         "date":"2/2/61",
#         "time":"10:00-11:00"
#       },
#       { 
#         "room":"6275",
#         "date":"3/2/61",
#         "time":"11:00-13:00"
#       }
      
#     ]
#   }
print(A.SendRegister("ton123","1234"))
print(A.SendLogin("ton123","1234"))
# print(A.SendBook(data))
# print(A.SendCancel(data))

# print(A.SendLogin("ton123","1234"))
# print(A.get_user())
# A=getipfromfile("config.txt")