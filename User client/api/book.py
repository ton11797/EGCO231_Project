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
