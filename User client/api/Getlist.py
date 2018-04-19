import requests
import json
import uuid
import hashlib

def GetList(fileip):
    r= requests.get(fileip+"/list")
    return r.text
