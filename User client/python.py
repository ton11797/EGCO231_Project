from tkinter import *

import tkinter
from tkinter import ttk

# import requests

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
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19,command=lambda :self.show_frame("search_room")).pack(side=TOP, padx=5)
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

# class search_room(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
#         self.controller = controller
#         month = ttk.Combobox(self,width=10,state='readonly')
#         month.place(x=205,y=10)
#         month['value'] = ('-','มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม')
#         month.current(0)
#         #ปี
#         year = ttk.Combobox(self,width=5,state='readonly')
#         year.place(x=310,y=10)
#         year['value'] =['-']+[i for i in range(2561,2571)]
#         year.current(0)
#         #เวลา
#         list_time = ['-','07.00-08.00','08.00-09.00','09.00-10.00','10.00-11.00','11.00-12.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00','17.00-18.00','18.00-19.00','19.00-20.00','20.00-21.00','21.00-22.00']
#         time = ttk.Combobox(self,width=10,value = list_time,state='readonly')
#         time.place(x=400,y=10)
#         time.current(0)
#         button = Button(self,text = 'ค้นหา',command = lambda:self.search_list_room(room,day,month,year,time,list_time)).place(x=230,y=50)
class search_room(Frame):

    # def search_list_room(self,room,day,month,year,time,list_time):
    #     textarea = Text(self, height=18, width=60,background='skyblue')
    #     scrollbar = Scrollbar(textarea)
    #     scrollbar.place(x=463,y=0,height=290)
    #     textarea.place(x=5,y=90)
    #     textarea.config(yscrollcommand=scrollbar.set)
    #     scrollbar.config(command=textarea.yview)
    #     if day.get()!= 1 and month.get()!= '-' and year.get()!= 2561:#must choose dd/mm/yy
    #         if room.get()!='-' and time.get()!='-':
    #             text = "\n ห้อง = "+room.get()+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time.get()+"\n"+"------------------------------------------------------------\n"
    #             textarea.insert(END,text)
    #             #Button(textarea,text='จองห้อง',padx=30).place(x=200,y=30)

    #         elif(room.get()!='-'):
    #             a = 80
    #             for i in range(1,len(time['value'])):
    #                 text = "\n ห้อง = "+room.get()+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time['value'][i]+"\n"+"------------------------------------------------------------\n"
    #                 textarea.insert(END,text)
    #                 #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))
    #         elif(time.get()!= '-'):
    #             a = 80
    #             for i in range(1,len(room['value'])):
    #                 text = "\n ห้อง = "+room['value'][i]+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time.get()+"\n"+"------------------------------------------------------------\n"
    #                 textarea.insert(END,text)
    #                 #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))
    #         else :
    #             a =80
    #             for i in range(1,len(room['value'])):
    #                 for j in range(1,len(time['value'])):
    #                     text = "\n ห้อง = "+room['value'][i]+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time['value'][j]+"\n"+"------------------------------------------------------------\n"
    #                     textarea.insert(END,text)
    #                     #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(j-1)))
    def search_list_room(self,room,day,month,year,time,list_time):
        panewd = PanedWindow(self,height=18, width=60)
        scrollbar = Scrollbar(panewd)
        scrollbar.pack(side=RIGHT, fill=Y)
        i=0
        if day.get()!= 1 and month.get()!= '-' and year.get()!= 2561:#must choose dd/mm/yy
            if room.get()!='-' and time.get()!='-':
                panelb = PanedWindow(panewd,height=6,width=60)
                lb = Label(panelb,text="ห้อง = "+room.get()+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time.get()).grid(row=0,column=0)
            #     #Button(textarea,text='จองห้อง',padx=30).place(x=200,y=30)

            # elif(room.get()!='-'):
            #     a = 80
            #     for i in range(1,len(time['value'])):
            #         text = "\n ห้อง = "+room.get()+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time['value'][i]+"\n"+"------------------------------------------------------------\n"
            #         textarea.insert(END,text)
            #         #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))
            # elif(time.get()!= '-'):
            #     a = 80
            #     for i in range(1,len(room['value'])):
            #         text = "\n ห้อง = "+room['value'][i]+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time.get()+"\n"+"------------------------------------------------------------\n"
            #         textarea.insert(END,text)
            #         #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))
            # else :
            #     a =80
            #     for i in range(1,len(room['value'])):
            #         for j in range(1,len(time['value'])):
            #             text = "\n ห้อง = "+room['value'][i]+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time['value'][j]+"\n"+"------------------------------------------------------------\n"
            #             textarea.insert(END,text)
            #             #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(j-1)))
        
        panewd.place(x=5,y=90)        

    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller
        # data = json.loads(Jdata)
        #ห้อง
        room = ttk.Combobox(self,width=5,state='readonly')
        room.place(x=35,y=10)
        room['value'] = ('-','R231','R123')
        room.current(0)
        #วัน
        day = ttk.Combobox(self,width=5,state='readonly')
        day.place(x=115,y=10)
        day['value'] =['-']+ [i for i in range(1,32)]
        day.current(0)
        #เดือน
        month = ttk.Combobox(self,width=10,state='readonly')
        month.place(x=205,y=10)
        month['value'] = ('-','มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม')
        month.current(0)
        #ปี
        year = ttk.Combobox(self,width=5,state='readonly')
        year.place(x=310,y=10)
        year['value'] =['-']+[i for i in range(2561,2571)]
        year.current(0)
        #เวลา
        list_time = ['-','07.00-08.00','08.00-09.00','09.00-10.00','10.00-11.00','11.00-12.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00','17.00-18.00','18.00-19.00','19.00-20.00','20.00-21.00','21.00-22.00']
        time = ttk.Combobox(self,width=10,value = list_time,state='readonly')
        time.place(x=400,y=10)
        time.current(0)
        button = Button(self,text = 'ค้นหา',command = lambda:self.search_list_room(room,day,month,year,time,list_time)).place(x=230,y=50)


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

        #Label(self,text="เวลาสิ้นสุด").place(x=280,y=100)
        #combo4 = ttk.Combobox(self)
        #combo4.place(x=280,y=130)
        #combo4['values'] = ('15','17','6','0')

        Label(self,text="ชื่อนาสกุลผู้จอง").place(x=80,y=180)
        combo4 = Entry(self)
        combo4.place(x=80,y=210)

        textOption = Label(self,text="อุปกรณ์ที่ใช้")
        textOption.place(x=80,y=250)
        varVar1 = IntVar(self)
        R1 = Checkbutton(self, text="โปรเจตเตอร์",variable=varVar1,onvalue = 1, offvalue = 0).place(x=80,y=280)
        R2 = Checkbutton(self, text="คอมพิวเตอร์",onvalue = 1, offvalue = 0).place(x=170,y=280)
        R3 = Checkbutton(self, text="ไมโครโฟน",onvalue = 1, offvalue = 0).place(x=260,y=280)


        b1 = Button(self,text='ยืนยัน',command=lambda : self.Book(combo1,combo2,combo3,combo4,R1,R2,R3)).place(x=80,y=330)
        b2 = Button(self,text='ล้างข้อมูล',command=lambda :self.Clear(combo1,combo2,combo3,combo4,R1,R2,R3)).place(x=180,y=330)


    def Clear(self,combo1,combo2,combo3,combo4,R1,R2,R3):
        combo1.set('')
        combo2.set('')
        combo3.set('')
        combo4.delete(0,'end')

    def Book(self,combo1,combo2,combo3,combo4,R1,R2,R3):
        if combo1.get()!="" and combo2.get()!="" and combo3.get()!="" and combo4.get()!="":
            data={
                "available-room":[
                    {
                        "Room":"%s"%(combo1.get()),
                        "schedule":[
                            {
                                "Username":"%s"%(combo4.get()),
                                "Data_Time":[
                                    {
                                        "Date":"%s"%(combo2.get()),
                                        "Time":"%s"%(combo3.get())
                                    }
                                ]
                            }
                        ]
                    }
                ]
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





if __name__ == "__main__":

    home()


