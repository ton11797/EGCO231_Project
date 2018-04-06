import json
from pprint import pprint

def filter_function(Jdata,room,user,date):
    data= json.loads(Jdata)
    dataroom=[]
    allroom=[]
    for aroom in data['available-room']:
        if(room!=""):
            if(room==aroom['Room']):            
                for scheduleroom in aroom['schedule']:
                    dataroom.append(aroom['Room'])
                    if(user!=""):
                        if(user==scheduleroom['Username']):
                            dataroom.append(scheduleroom['Username'])
                            if(date!=""):
                                for word in scheduleroom['Data Time'].split():
                                    if(word==date):
                                        dataroom.append(scheduleroom['Data Time'])
                                        allroom.append(dataroom)
                                        dataroom=[]
                                
                            else:
                            
                                dataroom.append(scheduleroom['Data Time'])
                                allroom.append(dataroom)
                                dataroom=[]
                            dataroom=[]
                    else:
                        dataroom.append(scheduleroom['Username'])
                        if(date!=""):
                            for word in scheduleroom['Data Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data Time'])
                                    allroom.append(dataroom)
                                    dataroom=[]
                        else:
                            dataroom.append(scheduleroom['Data Time'])
                            allroom.append(dataroom)
                            dataroom=[]
                        dataroom=[]
                    dataroom=[]
        else:
        
            for scheduleroom in aroom['schedule']:
                dataroom.append(aroom['Room'])
                if(user!=""):
                    if(user==scheduleroom['Username']):
                        dataroom.append(scheduleroom['Username'])
                        if(date!=""):
                            for word in scheduleroom['Data Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data Time'])
                                    allroom.append(dataroom)
                                    dataroom=[]
                                
                        else:
                            
                            dataroom.append(scheduleroom['Data Time'])
                            allroom.append(dataroom)
                            dataroom=[]
                        dataroom=[]
                else:
                    dataroom.append(scheduleroom['Username'])
                    if(date!=""):
                        for word in scheduleroom['Data Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data Time'])
                                    allroom.append(dataroom)
                                    dataroom=[]
                    else:
                        dataroom.append(scheduleroom['Data Time'])
                        allroom.append(dataroom)
                        dataroom=[]
                    dataroom=[]
                dataroom=[]
    return allroom
    

      
   

