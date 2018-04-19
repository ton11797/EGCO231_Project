import control
import api
import json
class center_control:
    def __init__(self):
        self.config = api.getipfromfile("config.txt")
    
    def SendBook_c(self,Data):
        api.SendBook(Data,self.config)
    

data ={
    "Data":[
      { 
        "room":"6275",
        "date":"4/2/61",
        "time":"08:00-11:00"
      },
      { 
        "room":"6275",
        "date":"4/2/61",
        "time":"10:00-11:00"
      },
      { 
        "room":"6275",
        "date":"5/2/61",
        "time":"11:00-13:00"
      }
      
    ],
    "cookie_session":"X6OP9B3TjhXd1GyXI1u22bC0snEXTKQ10402044846"
  }
  

CC = center_control()
print(CC.SendBook_c((data)))