from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
import json
import api
A = api.API_cen()

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

class search_room(Frame):

    def search_list_room(self,room,day,month,year,time,list_time):
        self.canvas.delete("1.0",END)
        date = (day.get()+"/"+str(month.current())+"/"+year.get())
        check = [day.get(),str(month.current()),year.get()]
        if '' in check:
            date = ''
        filtered_data=filter_function(A.GetList(),room.get(),"",date)

        for f_data in filtered_data:
            a = 80
            dtime = f_data[2].split()
            text = "\n ห้อง \t: "+f_data[0]+"\n"+" วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            self.canvas.insert(END,text)
            #Button(self.textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))

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
        #self.textarea = Frame(self,background='#283149')
        #self.textarea.place(x=15,y=90)
        #self.scrollbar = Scrollbar(self.textarea,orient= VERTICAL)

        self.subframe = Frame(self,height=300, width= 460)
        self.subframe.place(x=15,y=90)

        self.canvas = Canvas(self.subframe,height=300, width= 460,bg='#283149',scrollregion=(0,0,500,500))
        #self.canvas.place(x=15,y=90)
        vbar=Scrollbar(self.subframe,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        
        vbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
        
        #self.scrollbar.config(command = self.canvas.yview)

        #pack
        #self.scrollbar.pack(side= RIGHT, fill= Y,  expand= FALSE)
        #self.canvas.pack(side= LEFT, padx=2, pady=2,fill= BOTH, expand= TRUE)

        self.filtered_data=filter_function(A.GetList(),"","","")
        space = 0
        for f_data in self.filtered_data:
            dtime = f_data[2].split()
            text = "\n ห้อง \t: "+f_data[0]+"\n"+"วัน/เดือน/ปี\t: "+dtime[0]+" "+"\n"+" เวลา \t: "+ dtime[1] +"\n"+" ผู้จอง \t: "+ f_data[1] +"\n"
            lb = Button(self.canvas,text = text, borderwidth=3, relief="groove",background='#FEF2BF', justify=LEFT,anchor = 'w')
            lb.place(x=17,y=20 + space,width=430)
            space +=110

        # scrollbar = Scrollbar( self.canvas )
        # scrollbar.place( x=30,y=90 )
        # scrollbar.config( command = self.canvas.yview )
        




class reserve_room(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller

        Label(self,text="เลือกห้องประชุม").place(x=80,y=20)
        combo1 = ttk.Combobox(self)
        combo1.place(x=80,y=50)
        combo1['values'] = ('15','17','6','0')

        Label(self,text="เลือกวัน").place(x=280,y=20)
        combo2 = ttk.Combobox(self)
        combo2.place(x=280,y=50)
        combo2['values'] = ('15','17','6','0')

        Label(self,text="เวลาเริ่มต้น").place(x=80,y=100)
        combo3 = ttk.Combobox(self)
        combo3.place(x=80,y=130)
        combo3['values'] = ('15','17','6','0')

        widget = Calendar(self)
        widget.place(x=280,y=130)


        Label(self,text="ชื่อนาสกุลผู้จอง").place(x=80,y=180)
        combo4 = Entry(self)
        combo4.place(x=80,y=210)

        textOption = Label(self,text="อุปกรณ์ที่ใช้")
        textOption.place(x=80,y=250)
        varVar1 = IntVar(self)
        R1 = Checkbutton(self, text="โปรเจตเตอร์",variable=varVar1,onvalue = 1, offvalue = 0).place(x=80,y=280)
        R2 = Checkbutton(self, text="คอมพิวเตอร์",onvalue = 1, offvalue = 0).place(x=170,y=280)
        R3 = Checkbutton(self, text="ไมโครโฟน",onvalue = 1, offvalue = 0).place(x=260,y=280)


        b1 = Button(self,text='ยืนยัน',command=lambda : self.Book(combo1,combo2,combo3,combo4,widget,R2,R3)).place(x=80,y=330)
        b2 = Button(self,text='ล้างข้อมูล',command=lambda :self.Clear(combo1,combo2,combo3,combo4,R1,R2,R3)).place(x=180,y=330)


    def Clear(self,combo1,combo2,combo3,combo4,R1,R2,R3):
        combo1.set('')
        combo2.set('')
        combo3.set('')
        combo4.delete(0,'end')

    def Book(self,combo1,combo2,combo3,combo4,widget,R2,R3):
        print (widget.selection_get())
        if combo1.get()!="" and combo2.get()!="" and combo3.get()!="" and combo4.get()!="":
            data={
                "Data":[
                    {
                        "room":"%s"%(combo1.get()),
                        "date":"%s"%(combo2.get()),
                        "time":"%s"%(combo3.get())
                    },
                ],

            }

            #send data
            #headers = {'Content-Type': 'application/json'}
            #reaponse = requests.post(fileip+"/book",headers=headers,data= json.dumps(DATA))
            #return reaponse.text

class cancel_room(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller
        labelfont = ('times', 20, 'bold')
        labelfont1 = ('times', 10)
        #Button(mainFrame1, text='จองห้อง',relief="flat",padx=9).pack(side=TOP, padx=5)
        label = Label(self, text='ห้องที่จองไว้',font=labelfont);
        label.place(x=10,y=10)
        EiB=Button(self, text='ยกเลิกห้อง',relief="flat",padx=9,pady=20)#.pack(side=TOP, padx=10,pady=10)
        EiB.place(x=350,y=70)
        label1 = Label(self, text='ห้อง',font=labelfont1);
        label1.place(x=100,y=50)
        label2 = Label(self, text='วัน',font=labelfont1);
        label2.place(x=100,y=70)
        label3 = Label(self, text='เวลา',font=labelfont1);
        label3.place(x=100,y=90)


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





if __name__ == "__main__":

    home()


