from tkinter import *
from tkinter import ttk
import tkinter
import json
#import pygtk
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
        self.show_frame("search_room")
        # run
        self.mainloop()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class search_room(Frame):

    def search_list_room(self,room,day,month,year,time,list_time):
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
                            textarea.insert(END,text)
                            #Button(textarea, text='จองห้อง',padx=30).place(x=200,y=30+(a*(j-1)))
    
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



class cancel_room(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)
        self.controller = controller



if __name__ == "__main__":
    home()








#def cancelnaja() :
 #   print("CencelNa")
