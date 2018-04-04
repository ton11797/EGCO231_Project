import json
from pprint import pprint
def printdataroom(data):
    print("Room : "+data[0])
    print("User : "+data[1])
    print("Data Time : "+data[2])
    print(" ")
def filter_function(Jdata,room,user,date):
    data= json.loads(Jdata)
    dataroom=[]
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
                                        printdataroom(dataroom)
                                        dataroom=[]
                                
                            else:
                            
                                dataroom.append(scheduleroom['Data Time'])
                                printdataroom(dataroom)
                                dataroom=[]
                            dataroom=[]
                    else:
                        dataroom.append(scheduleroom['Username'])
                        if(date!=""):
                            for word in scheduleroom['Data Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data Time'])
                                    printdataroom(dataroom)
                                    dataroom=[]
                        else:
                            dataroom.append(scheduleroom['Data Time'])
                            printdataroom(dataroom)
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
                                    printdataroom(dataroom)
                                    dataroom=[]
                                
                        else:
                            
                            dataroom.append(scheduleroom['Data Time'])
                            printdataroom(dataroom)
                            dataroom=[]
                        dataroom=[]
                else:
                    dataroom.append(scheduleroom['Username'])
                    if(date!=""):
                        for word in scheduleroom['Data Time'].split():
                                if(word==date):
                                    dataroom.append(scheduleroom['Data Time'])
                                    printdataroom(dataroom)
                                    dataroom=[]
                    else:
                        dataroom.append(scheduleroom['Data Time'])
                        printdataroom(dataroom)
                        dataroom=[]
                    dataroom=[]
                dataroom=[]    

data = '''
{
  "available-room": [
    {
      "Room": "6272",
      "schedule": [
        {
          "Username": "narit",
          "Data Time": "25/4/2561 12:00-16:00"
        },
        {
          "Username": "narit",
          "Data Time": "28/4/2561 09:00-12:00"
        },
        {
          "Username": "gift",
          "Data Time": "30/4/2561 09:00-12:00"
        }
      ]
    },
    {
      "Room": "6273",
      "schedule": [
        {
          "Username": "mook",
          "Data Time": "16/4/2561 12:00-16:00"
        },
        {
          "Username": "pear",
          "Data Time": "11/4/2561 09:00-12:00"
        }
      ]
    },
    {
      "Room": "6274",
      "schedule": [
        {
          "Username": "jane",
          "Data Time": "24/4/2561 09:00-12:00"
        },
        {
          "Username": "ton",
          "Data Time": "10/4/2561 09:00-12:00"
        }
      ]
    }
  ]
}
'''


room=input("Room : ")
user=input("User : ")
date=input("Date : ")
filter_function(data,room,user,date)




