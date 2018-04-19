import json
from pprint import pprint
import api

A = api.API_cen()


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
                        if(user==scheduleroom['username']):
                            dataroom.append(scheduleroom['username'])
                            if(date!=""):
                                if date == scheduleroom['date']:
                                    Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                                    dataroom.append(Date_Time)
                                    allroom.append(dataroom)
                                    dataroom=[]
                                
                            else:
                                Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                                dataroom.append(Date_Time)
                                allroom.append(dataroom)
                                dataroom=[]
                            dataroom=[]
                    else:
                        dataroom.append(scheduleroom['username'])
                        if(date!=""):
                            if date == scheduleroom['date']:
                                Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                                dataroom.append(Date_Time)
                                allroom.append(dataroom)
                                dataroom=[]
                        else:
                            Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                            dataroom.append(Date_Time)
                            allroom.append(dataroom)
                            dataroom=[]
                        dataroom=[]
                    dataroom=[]
        else:
        
            for scheduleroom in aroom['schedule']:
                dataroom.append(aroom['room'])
                if(user!=""):
                    if(user==scheduleroom['username']):
                        dataroom.append(scheduleroom['username'])
                        if(date!=""):
                            if date == scheduleroom['date']:
                                Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                                dataroom.append(Date_Time)
                                allroom.append(dataroom)
                                dataroom=[]
                                
                        else:
                            dataroom.append(scheduleroom['Data_Time'])
                            allroom.append(dataroom)
                            dataroom=[]
                        dataroom=[]
                else:
                    dataroom.append(scheduleroom['username'])
                    if(date!=""):
                            if date == scheduleroom['date']:
                                Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                                dataroom.append(Date_Time)
                                allroom.append(dataroom)
                                dataroom=[]
                    else:
                        Date_Time = (scheduleroom['date'] +" "+scheduleroom['time'])
                        dataroom.append(Date_Time)
                        allroom.append(dataroom)
                        dataroom=[]
                    dataroom=[]
                dataroom=[]
    return allroom

# data = json.dump(open('input.json'))
#print(A.SendLogin("ton123","1234"))
#print(A.GetList())
data = A.GetList()
print(data)
print(filter_function(data,"6272","","" ))
   

