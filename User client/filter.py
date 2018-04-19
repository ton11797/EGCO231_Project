import json
from pprint import pprint

def filter_function(Jdata,room,user,date):
    data= json.loads(Jdata)
    dataroom=[]
    allroom=[]
    for aroom in data['available-room']:
        if(room!=""):
            if(room==aroom['room']):            
                for scheduleroom in aroom['schedule']:
                    dataroom.append(aroom['room'])
                    if(user!=""):
                        if(user==scheduleroom['Username']):
                            dataroom.append(scheduleroom['Username'])
                            if(date!=""):
                                for word in scheduleroom['Data_Time'].split():
                                    if(word==date):
                                        dataroom.append(scheduleroom['Data_Time'])
                                        allroom.append(dataroom)
                                        dataroom=[]
                                
                            else:
                            
                                dataroom.append(scheduleroom['Data_Time'])
                                allroom.append(dataroom)
                                dataroom=[]
                            dataroom=[]
                    else:
                        dataroom.append(scheduleroom['Username'])
                        if(date!=""):
                            for word in scheduleroom['Data_Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data_Time'])
                                    allroom.append(dataroom)
                                    dataroom=[]
                        else:
                            dataroom.append(scheduleroom['Data_Time'])
                            allroom.append(dataroom)
                            dataroom=[]
                        dataroom=[]
                    dataroom=[]
        else:
        
            for scheduleroom in aroom['schedule']:
                dataroom.append(aroom['room'])
                if(user!=""):
                    if(user==scheduleroom['Username']):
                        dataroom.append(scheduleroom['Username'])
                        if(date!=""):
                            for word in scheduleroom['Data_Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data_Time'])
                                    allroom.append(dataroom)
                                    dataroom=[]
                                
                        else:
                            
                            dataroom.append(scheduleroom['Data_Time'])
                            allroom.append(dataroom)
                            dataroom=[]
                        dataroom=[]
                else:
                    dataroom.append(scheduleroom['Username'])
                    if(date!=""):
                        for word in scheduleroom['Data_Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data_Time'])
                                    allroom.append(dataroom)
                                    dataroom=[]
                    else:
                        dataroom.append(scheduleroom['Data_Time'])
                        allroom.append(dataroom)
                        dataroom=[]
                    dataroom=[]
                dataroom=[]
    return allroom
    
jdata = (open('input.json')).read()
print(filter_function(jdata,"","",""))