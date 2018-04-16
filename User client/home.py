from tkinter import *
import requests
import tkinter

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
        self.room_list = requests.get(fileip+"/list")

        # run
        self.mainloop()
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class search_room(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller
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

    def search_list_room(self,room,day,month,year,time,list_time):
        #filtered_data=filter_function(raw_data,room=room,date=day+month+year)

        textarea = Text(self, height=18, width=60,background='skyblue')
        scrollbar = Scrollbar(textarea)
        scrollbar.place(x=463,y=0,height=290)
        textarea.place(x=5,y=90)
        textarea.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textarea.yview)
        if day.get()!= 1 and month.get()!= '-' and year.get()!= 2561:#must choose dd/mm/yy
            if room.get()!='-' and time.get()!='-':
                text = "\n ห้อง = "+room.get()+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time.get()+"\n"+"------------------------------------------------------------\n"
                textarea.insert(END,text)
                #Button(textarea,text='จองห้อง',padx=30).place(x=200,y=30)

            elif(room.get()!='-'):
                a = 80
                for i in range(1,len(time['value'])):
                    text = "\n ห้อง = "+room.get()+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time['value'][i]+"\n"+"------------------------------------------------------------\n"
                    textarea.insert(END,text)
                    #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))
            elif(time.get()!= '-'):
                a = 80
                for i in range(1,len(room['value'])):
                    text = "\n ห้อง = "+room['value'][i]+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time.get()+"\n"+"------------------------------------------------------------\n"
                    textarea.insert(END,text)
                    #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(i-1)))
            else :
                a =80
                for i in range(1,len(room['value'])):
                    for j in range(1,len(time['value'])):
                        text = "\n ห้อง = "+room['value'][i]+"\n"+" วัน/เดือน/ปี="+day.get()+" "+month.get()+" "+year.get()+"\n"+" เวลา = "+time['value'][j]+"\n"+"------------------------------------------------------------\n"




class reserve_room(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller
        

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


