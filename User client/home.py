from tkinter import ttk
from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import json
import api
import time
import os
import datetime

myfile="./tmp"
A = api.API_cen()
if not(os.path.isfile(myfile)):
    exit()
A.read_login()

#############################################################################################################
#variable theme 
#Color = ["#282828","#070705","#84e611","#50524d",'white']  #GreenForce
#Color = ["#283149","#404B69","#F73859","#DBEDF3",'white'] #Candle
Color = ["white","#404B69","#b0fb45","#DBEDF3",'black'] #mongo color

def font(size = 15):
    return ("Codia new",size,"bold")

#############################################################################################################
#Home to show frame
class home(Tk):

    def __init__(self):
        Tk.__init__(self)
        containner=Frame(self,bg = Color[1])
        containner.pack()
        menuList = Frame(containner, relief=SUNKEN)
        self.frames = {}
        for F in (search_room, reserve_room, cancel_room):
            page_name = F.__name__
            print(page_name)
            frame = F(parent=containner,controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=1,rowspan=10)
        
        def Botton_Create(frame,text,show_frame):
            btn = Button(frame, text= text,relief="flat",font = font(),
                    height = 5,width = 10,fg = 'white',
                    command=lambda :self.show_frame(btn,show_frame))
            btn.pack(side = TOP,fill = X)
            return btn
        self.b1 = Botton_Create(menuList,'จองห้อง',"reserve_room")
        self.b2 = Botton_Create(menuList,'ตรวจสอบห้อง',"search_room")
        self.b3 = Botton_Create(menuList,'ยกเลิกการจอง',"cancel_room")

        menuList.grid( row=0,column=0)
        self.show_frame(self.b1,"reserve_room")
        #get roomlist
        # self.room_list = requests.get(fileip+"/list")

        # run
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()
    
    def show_frame(self, btn,page_name):
        self.b1['background'] = Color[1]
        self.b1['foreground'] = 'white'
        self.b2['background'] = Color[1]
        self.b2['foreground'] = 'white'
        self.b3['background'] = Color[1]
        self.b3['foreground'] = 'white'
        btn['background'] = Color[2]
        btn['foreground'] = 'black'
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        if os.path.isfile(myfile):
            os.remove(myfile)
        self.destroy()
#############################################################################################################
#Scrollbar Frame
class Scrollable(ttk.Frame):

    def __init__(self, frame, width=16):
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame,width = 420,height = 280,bg = Color[3],yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame,bg = Color[3])         

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self,anchor=tk.NW)

    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)        

    def update(self):
        "Update the canvas and the scrollregion"
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
#############################################################################################################   
#Frame Search_room
class search_room(Frame):

    def search_list_room(self,room,day,month,year):
        for widget in self.scrollable_body.winfo_children():
            widget.destroy()
        date = ''
        check = [day.get(),str(month.current()),year.get()]
        if not('' in check):
            dday = day.get()
            dmonth = str(month.current())
            if int(day.get()) < 10 :
                dday = ("0"+day.get())
            if int(month.current()) < 10:
                dmonth = ("0"+str(month.current()))
            date = (dday+"/"+dmonth+"/"+year.get())
            if dmonth == "00":
                date = ''
        print(date)

        filtered_data=filter_function(A.GetList(),room.get(),"",date)
        for f_data in filtered_data:
            dtime = f_data[2].split()
            time_s = dtime[1].split('-')
            dd,mm,yy = str(dtime[0]).split("/")
            validatetime = yy+"-"+mm+"-"+dd+" "+time_s[0]
            timestamp = time.mktime(datetime.datetime.strptime(validatetime, "%Y-%m-%d %H:%M").timetuple())
            if time.time() < timestamp:#ถ้าเวลาจริง น้อยกว่า เวลาที่จอง ->จองอนาคต
                text = "ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1]
                Button(self.scrollable_body,text = text,font =font(),bg=Color[2],width = 35, 
                        justify=LEFT,anchor = 'w').grid(sticky="WE")
        self.scrollable_body.update()

    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400,bg = Color[0])
        self.controller = controller

        #ห้อง
        lb = Label(self,text = 'ห้อง',font =font(),bg = Color[0],fg = Color[4]).place(x=10,y=10)
        room = ttk.Combobox(self,width = 10,state='readonly')
        room.place(x= 10+35,y=10)
        room['value'] = ('','6272','6273','6274',"6275","6276","309/1","309/2","310","meeting room")
        room.current(0)
        #วัน
        lb = Label(self,text = 'วัน/เดือน/ปี',font =font(),bg = Color[0],fg = Color[4])
        lb.place(x=130,y=10)
        day = ttk.Combobox(self,width=5,state='readonly')
        day.place(x=215,y=10)
        day['value'] =['']+ [i for i in range(1,32)]
        day.current(0)
        #เดือน
        month = ttk.Combobox(self,width=10,state='readonly')
        month.place(x=90+205,y=10)
        month['value'] = ('','มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม')
        month.current(0)
        #ปี
        year = ttk.Combobox(self,width=5,state='readonly')
        year.place(x= 400,y=10)
        year['value'] =['']+[i for i in range(2018,2029)]
        year.current(0)

        Button(self,text = 'ค้นหา',font = font(),bg =  Color[2],relief = FLAT,
                command = lambda:self.search_list_room(room,day,month,year)).place(x=230,y=50)
        #show
        self.subframe = Frame(self,bg = Color[3],relief=FLAT)
        self.subframe.place(x=20,y=100)

        self.scrollable_body = Scrollable(self.subframe)        
        self.filtered_data=filter_function(A.GetList(),"","","")
        for f_data in self.filtered_data:
            dtime = f_data[2].split()
            time_s = dtime[1].split('-')
            dd,mm,yy = str(dtime[0]).split("/")
            validatetime = yy+"-"+mm+"-"+dd+" "+time_s[0]
            timestamp = time.mktime(datetime.datetime.strptime(validatetime, "%Y-%m-%d %H:%M").timetuple())
            if time.time() < timestamp:#ถ้าเวลาจริง น้อยกว่า เวลาที่จอง ->จองอนาคต
                text = "ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1]
                Button(self.scrollable_body,text = text,font =font(),bg=Color[2],width = 35, 
                        justify=LEFT,anchor = 'w').grid(sticky="WE")
        
        self.scrollable_body.update()
####################################################################################################################
#Frame Reserve_room
class reserve_room(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400,bg = Color[0])
        self.controller = controller

        Label(self,text="เลือกห้องประชุม",font = font(),bg = Color[0],fg = Color[4]).place(x=80,y=20)
        room = ttk.Combobox(self,state='readonly')
        room.place(x=80,y=50)
        room['value'] = ('','6272','6273','6274',"6275","6276","309/1","309/2","310","meeting room")

        Label(self,text="เลือกเวลา",font = font(),bg = Color[0],fg = Color[4]).place(x=280,y=20)
        begin_time = ttk.Combobox(self,width=5,state='readonly')
        begin_time.place(x=280,y=50)
        begin_time['values'] = ["07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"]

        Label(self,text="ถึง",font = font(),bg = Color[0],fg = Color[4]).place(x=340,y=45)

        end_time = ttk.Combobox(self,width=5,state='readonly')
        end_time.place(x=370,y=50)
        end_time['values'] = ["07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"]

        Label(self,text="เลือกวัน",font = font(),bg = Color[0],fg = Color[4]).place(x=80,y=100)
        date = Calendar(self)
        date.place(x=130,y=130)
        Button(self,text='ยืนยัน',width = 10,relief = FLAT,font = font(),bg = Color[2],
                command=lambda : self.Book(room,begin_time,end_time,date)).place(x=100,y=330)
        Button(self,text='ล้างข้อมูล',width = 10,relief = FLAT,font = font(),bg = Color[2],
                command=lambda :self.Clear(room,begin_time,end_time,date)).place(x=280,y=330)


    def Clear(self,room,begin_time,end_time,date):
        room.set('')
        begin_time.set('')
        end_time.set('')


    def Book(self,room,begin_time,end_time,date):
        import datetime
        now = datetime.datetime.now()
        print (date.selection_get())
        if room.get()=="" or begin_time.get()=="" or end_time.get()=="":
            tm.showinfo("Warning", "กรอกข้อมูลไม่ครบ")
            return ""
        if end_time.get() <= begin_time.get():
            tm.showinfo("Warning", "เวลาไม่ถูกต้อง")
            return ""

        yy,mm,dd = str(date.selection_get()).split("-")
        data_ = dd+"/"+mm+"/"+yy
        validatetime = yy+"-"+mm+"-"+dd+" "+begin_time.get()
        timestamp = time.mktime(datetime.datetime.strptime(validatetime, "%Y-%m-%d %H:%M").timetuple())
        if time.time() > timestamp: #ถ้าเวลาจริง มากกว่า เวลาที่จอง
            tm.showinfo("Warning", "วันที่ไม่ถูกต้อง")
            return ""

        if room.get()!="" and begin_time.get()!="" and end_time.get()!="":
            data={
                "Data":[
                    {
                        "room":"%s"%(room.get()),
                        "date":"%s"%(data_),
                        "time":"%s"%(begin_time.get()+"-"+end_time.get())
                    },
                ],

            }
            status = json.loads(A.SendBook(data))['respond'][0]
            if (status['status']=="sucess"):
                tm.showinfo("BOOK info", "Done")
            else:
                tm.showerror("BOOK error", status['error'])
            #send data
            #headers = {'Content-Type': 'application/json'}
            #reaponse = requests.post(fileip+"/book",headers=headers,data= json.dumps(DATA))
            #return reaponse.text
#############################################################################################################
#Frame cancel_room
class cancel_room(Frame):
    def reload(self):
        print("cal")
        for widget in self.scrollable_body.winfo_children():
            widget.destroy()
        if A.get_user()=="admin":
            filtered_data=filter_function(A.GetList(),"","","")
        else:
            filtered_data=filter_function(A.GetList(),"",A.get_user(),"")
        for f_data in filtered_data:
            dtime = f_data[2].split()
            data = []
            a=(f_data[0])
            b=(f_data[1])
            c=(dtime[0])
            d=(dtime[1])
            text = "ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1]
            Button(self.scrollable_body,text = text,font =font(),bg=Color[2],width = 35, 
                        justify=LEFT,anchor = 'w',
                        command = lambda a=a,b=b,c=c,d=d:self.cancel_data(a,b,c,d)).grid(sticky="WE")
        self.scrollable_body.update()
    def cancel_data(self,a,b,c,d):
        datadic ={}
        datadic['Data']=[]
        datadic['Data'].append({"room":a,"date":c,"time":d})
        A.SendCancel(datadic)
        print(a+" "+b+" "+c+" "+d)
        print(datadic)
        for widget in self.scrollable_body.winfo_children():
            widget.destroy()
        if A.get_user()=="admin":
            filtered_data=filter_function(A.GetList(),"","","")
        else:
            filtered_data=filter_function(A.GetList(),"",A.get_user(),"")
        for f_data in filtered_data:
            dtime = f_data[2].split()
            data = []
            a=(f_data[0])
            b=(f_data[1])
            c=(dtime[0])
            d=(dtime[1])
            text = "ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1]
            Button(self.scrollable_body,text = text,font =font(),bg=Color[2],width = 35, 
                        justify=LEFT,anchor = 'w',
                        command = lambda a=a,b=b,c=c,d=d:self.cancel_data(a,b,c,d)).grid(sticky="WE")
        self.scrollable_body.update()
        print("DONE")
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400,bg = Color[0])
        self.controller = controller

        label = Label(self, text='ยกเลิกห้องที่จองไว้',font=font(20),bg = Color[0],fg = Color[4])
        label.place(x=10,y=10)
        Button(self,text='โหลดใหม่',font = font(),bg = Color[2],relief = FLAT,
                command=lambda : self.reload()).place(x=300,y=15)
        #show
        self.subframe = Frame(self,bg = Color[3],relief=FLAT)
        self.subframe.place(x=20,y=100)

        self.scrollable_body = Scrollable(self.subframe, width=30)
        if A.get_user()=="admin":
            self.filtered_data=filter_function(A.GetList(),"","","")
        else:
            self.filtered_data=filter_function(A.GetList(),"",A.get_user(),"")
        i =0
        for f_data in self.filtered_data:
            dtime = f_data[2].split()
            data = []
            a=(f_data[0])
            b=(f_data[1])
            c=(dtime[0])
            d=(dtime[1])
            text = "ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1]
            Button(self.scrollable_body,text = text,font =font(),bg=Color[2],width = 35, 
                        justify=LEFT,anchor = 'w',
                        command = lambda a=a,b=b,c=c,d=d:self.cancel_data(a,b,c,d)).grid(sticky="WE")
        self.scrollable_body.update()
#######################################################################################################################
# filter method 
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
    return allroom
#############################################################################################################

if __name__ == "__main__":

    home()


