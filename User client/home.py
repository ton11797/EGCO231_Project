from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import json
import api
import time
A = api.API_cen()
A.SendLogin("ton1234","ton1234")
A.read_login()
class home(Tk):

    def __init__(self):
        Tk.__init__(self)
        containner=Frame(self)
        containner.pack()
        menuList = Frame(containner, relief=SUNKEN)
        self.frames = {}
        for F in (search_room, reserve_room, cancel_room):
            page_name = F.__name__
            print(page_name)
            frame = F(parent=containner,controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=1,rowspan=10)
        Button(menuList, text='จองห้อง',relief="flat",padx=39,command=lambda :self.show_frame("reserve_room")).pack(side=TOP, padx=5)
        Button(menuList, text='ตรวจสอบห้อง',relief="flat",padx=19,command=lambda :self.show_frame("search_room")).pack(side=TOP, padx=5)
        Button(menuList, text='ยกเลิกการจอง',relief="flat",padx=20,command=lambda :self.show_frame("cancel_room")).pack(side=TOP, padx=5)
        menuList.grid( row=0,column=0,pady=10, padx=5)
        self.show_frame("reserve_room")
        #get roomlist
        # self.room_list = requests.get(fileip+"/list")

        # run
        self.mainloop()
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

##########################################################################
class Scrollable(ttk.Frame):

    def __init__(self, frame, width=16):
        scrollbar = tk.Scrollbar(frame,width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame,bg = "#283149",yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame,bg = "#283149")         

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
################################################################################################        

class search_room(Frame):

    def search_list_room(self,room,day,month,year,time,list_time):
        for widget in self.scrollable_body.winfo_children():
            widget.destroy()
        
        date = (day.get()+"/"+str(month.current())+"/"+year.get())
        check = [day.get(),str(month.current()),year.get()]
        if '' in check:
            date = ''
        filtered_data=filter_function(A.GetList(),room.get(),"",date)
        for f_data in filtered_data:
            dtime = f_data[2].split()
            text = "\n ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\t\t\t\t\t\t\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            Button(self.scrollable_body,text = text,bg='#F73859', justify=LEFT,anchor = 'w',relief=SUNKEN).grid(sticky="WE")
        self.scrollable_body.update()

    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller

        #ห้อง
        room = ttk.Combobox(self,width=5,state='readonly')
        room.place(x=35,y=10)
        room['value'] = ('','6272','6273','6274',"6275","6276","309/1","309/2","310")
        room.current(0)
        #วัน
        day = ttk.Combobox(self,width=5,state='readonly')
        day.place(x=115,y=10)
        day['value'] =['']+ [i for i in range(1,32)]
        day.current(0)
        #เดือน
        month = ttk.Combobox(self,width=10,state='readonly')
        month.place(x=205,y=10)
        month['value'] = ('','มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม')
        month.current(0)
        #ปี
        year = ttk.Combobox(self,width=5,state='readonly')
        year.place(x=310,y=10)
        year['value'] =['']+[i for i in range(2561,2571)]
        year.current(0)
        #เวลา
        list_time = ['','07.00-08.00','08.00-09.00','09.00-10.00','10.00-11.00','11.00-12.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00','17.00-18.00','18.00-19.00','19.00-20.00','20.00-21.00','21.00-22.00']
        time = ttk.Combobox(self,width=10,value = list_time,state='readonly')
        time.place(x=400,y=10)
        time.current(0)
        Button(self,text = 'ค้นหา',command = lambda:self.search_list_room(room,day,month,year,time,list_time)).place(x=230,y=50)
        #show
        self.subframe = Frame(self,bg = "#283149",relief=SUNKEN)
        self.subframe.place(x=15,y=90)

        self.scrollable_body = Scrollable(self.subframe, width=30)        
        self.filtered_data=filter_function(A.GetList(),"","","")
        for f_data in self.filtered_data:
            dtime = f_data[2].split()
            text = "\n ห้อง \t: "+f_data[0]+"\t\t\t\t\t\t\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\t\t\t\t\t\t\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            Button(self.scrollable_body,text = text,bg='#F73859', justify=LEFT,anchor = 'w').grid(sticky="WE")
        
        self.scrollable_body.update()



class reserve_room(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller

        Label(self,text="เลือกห้องประชุม").place(x=80,y=20)
        room = ttk.Combobox(self)
        room.place(x=80,y=50)
        room['value'] = ('','6272','6273','6274',"6275","6276","309/1","309/2","310")

        Label(self,text="เลือกเวลา").place(x=280,y=20)
        begin_time = ttk.Combobox(self,width=5)
        begin_time.place(x=280,y=50)
        begin_time['values'] =['-']+["07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"]

        Label(self,text="ถึง").place(x=340,y=50)

        end_time = ttk.Combobox(self,width=5)
        end_time.place(x=370,y=50)
        end_time['values'] =['-']+["07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"]

        Label(self,text="เลือกวัน").place(x=80,y=100)
        date = Calendar(self,width=20,height=100)
        date.place(x=80,y=130)









        Button(self,text='ยืนยัน',command=lambda : self.Book(room,begin_time,end_time,date)).place(x=80,y=330)
        Button(self,text='ล้างข้อมูล',command=lambda :self.Clear(room,begin_time,end_time,date)).place(x=180,y=330)


    def Clear(self,room,begin_time,end_time,date):
        room.set('')
        begin_time.set('')
        end_time.set('')


    def Book(self,room,begin_time,end_time,date):
        print (date.selection_get())
        yy,mm,dd = str(date.selection_get()).split("-")
        print (dd+"/"+mm+"/"+yy)
        print(room.get())
        if room.get()!="" and begin_time.get()!="" and end_time.get()!="":
            data={
                "Data":[
                    {
                        "room":"%s"%(room.get()),
                        "date":"%s"%(begin_time.get()),
                        "time":"%s"%(end_time.get())
                    },
                ],

            }
            print(data)
            A.SendBook(data)
            #send data
            #headers = {'Content-Type': 'application/json'}
            #reaponse = requests.post(fileip+"/book",headers=headers,data= json.dumps(DATA))
            #return reaponse.text

class cancel_room(Frame):
    def reload(self):
        print("cal")
        for widget in self.scrollable_body.winfo_children():
            widget.destroy()
        filtered_data=filter_function(A.GetList(),"","ton1234","")
        for f_data in filtered_data:
            dtime = f_data[2].split()
            data = []
            a=(f_data[0])
            b=(f_data[1])
            c=(dtime[0])
            d=(dtime[1])
            text = "\n ห้อง \t: "+f_data[0]+"\t\t\t\t\t\t\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\t\t\t\t\t\t\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            Button(self.scrollable_body,text = text,bg='#F73859', justify=LEFT,anchor = 'w',command = lambda a=a,b=b,c=c,d=d:self.cancel_data(a,b,c,d)).grid(sticky="WE")
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
        filtered_data=filter_function(A.GetList(),"","ton1234","")
        for f_data in filtered_data:
            dtime = f_data[2].split()
            data = []
            a=(f_data[0])
            b=(f_data[1])
            c=(dtime[0])
            d=(dtime[1])
            text = "\n ห้อง \t: "+f_data[0]+"\t\t\t\t\t\t\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\t\t\t\t\t\t\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            Button(self.scrollable_body,text = text,bg='#F73859', justify=LEFT,anchor = 'w',command = lambda a=a,b=b,c=c,d=d:self.cancel_data(a,b,c,d)).grid(sticky="WE")
        self.scrollable_body.update()
        print("DONE")
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller
        labelfont = ('times', 20, 'bold')
        labelfont1 = ('times', 10)
        #Button(mainFrame1, text='จองห้อง',relief="flat",padx=9).pack(side=TOP, padx=5)
        label = Label(self, text='ยกเลิกห้องที่จองไว้',font=labelfont)
        label.place(x=10,y=10)
        Button(self,text='โหลดใหม่',command=lambda : self.reload()).place(x=300,y=15)
        #show
        self.subframe = Frame(self,bg = "#283149",relief=SUNKEN)
        self.subframe.place(x=15,y=90)

        self.scrollable_body = Scrollable(self.subframe, width=30)        
        self.filtered_data=filter_function(A.GetList(),"","ton1234","")
        i =0
        for f_data in self.filtered_data:
            dtime = f_data[2].split()
            data = []
            a=(f_data[0])
            b=(f_data[1])
            c=(dtime[0])
            d=(dtime[1])
            text = "\n ห้อง \t: "+f_data[0]+"\t\t\t\t\t\t\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\t\t\t\t\t\t\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            Button(self.scrollable_body,text = text,bg='#F73859', justify=LEFT,anchor = 'w',command = lambda a=a,b=b,c=c,d=d:self.cancel_data(a,b,c,d)).grid(sticky="WE")
        self.scrollable_body.update()


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





if __name__ == "__main__":

    home()


