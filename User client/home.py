from tkinter import *

import tkinter

def cancelnaja(mainFrame,self) :

    mainFrame1 = Frame(mainFrame,width=500, height=400, bd=1, relief=SUNKEN)

    mainFrame1.place(x=0,y=0)

    print("CencelNa")

    #mainFrame

    labelfont = ('times', 20, 'bold')

    labelfont1 = ('times', 10)

    #Button(mainFrame1, text='จองห้อง',relief="flat",padx=9).pack(side=TOP, padx=5)

    label = Label(mainFrame1, text='ห้องที่จองไว้',font=labelfont);

    label.place(x=10,y=10)

    EiB=Button(mainFrame1, text='จองห้อง',relief="flat",padx=9,pady=20)#.pack(side=TOP, padx=10,pady=10)

    EiB.place(x=350,y=70)

    label1 = Label(mainFrame1, text='ห้อง',font=labelfont1);

    label1.place(x=100,y=50)

    label2 = Label(mainFrame1, text='วัน',font=labelfont1);

    label2.place(x=100,y=70)

    label3 = Label(mainFrame1, text='เวลา',font=labelfont1);

    label3.place(x=100,y=90)



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



    def __init__(self, parent, controller):

        Frame.__init__(self,parent,width=500, height=400, bd=1, relief=SUNKEN)

        self.controller = controller









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


