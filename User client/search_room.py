from tkinter import *
from tkinter import ttk
class home(Tk):
    def __init__(self):
        Tk.__init__(self)
        menuList = Frame(self, relief=SUNKEN)
        mainFrame = Frame(self,width=500, height=400, bd=1, relief=SUNKEN)
        
        Button(menuList, text='จองห้อง',relief="flat",padx=39).pack(side=TOP, padx=5)
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19,command = lambda:self.search_room(mainFrame)).pack(side=TOP, padx=5)
        Button(menuList, text='ตารางการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5)
        menuList.pack( side=LEFT,fill=Y,pady=10, padx=5)
        mainFrame.pack(side=LEFT,expand=1, pady=10, padx=5)
        
    def search_list_room(self,mainFrame,combo1,combo2,combo3,combo4,combo5):
        label1 = Label(mainFrame,text = "ห้อง = "+combo1.get())
        label1.place(x=5,y=90)
        label2 = Label(mainFrame,text = "วัน = "+combo2.get())
        label2.place(x=5,y=110)
        label3 = Label(mainFrame,text = "เดือน = "+combo3.get())
        label3.place(x=5,y=130)
        label4 = Label(mainFrame,text = "ปี = "+combo4.get())
        label4.place(x=5,y=150)
        label5 = Label(mainFrame,text = "เวลา = "+combo5.get())
        label5.place(x=5,y=170)
        
        print(combo1.get()+"  ")
        print(combo2.get()+"  ")
        print(combo3.get()+"  ")
        print(combo4.get()+"  ")
        print(combo5.get()+"  ")
        print("\n")
        
        
    def search_room(self,mainFrame):
        label = Label(mainFrame,text ="ห้อง : ")
        label.place(x=5,y=10)
        label = Label(mainFrame,text ="วัน : ")
        label.place(x=90,y=10)
        label = Label(mainFrame,text ="เดือน : ")
        label.place(x=170,y=10)
        label = Label(mainFrame,text ="ปี : ")
        label.place(x=290,y=10)
        label = Label(mainFrame,text ="เวลา : ")
        label.place(x=365,y=10)
        #ห้อง
        combo1 = ttk.Combobox(mainFrame,width=5)
        combo1.place(x=35,y=10)
        combo1['value'] = ('R231')
        #วัน
        i = 0
        day  = list();
        while (i < 31):
            day.append(i+1)
            i = i + 1
        combo2 = ttk.Combobox(mainFrame,width=5,value = day)
        combo2.place(x=115,y=10)
        #เดือน
        combo3 = ttk.Combobox(mainFrame,width=10)
        combo3.place(x=205,y=10)
        combo3['value'] = ('มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม')
        #ปี
        i = 2549
        year  = list();
        while (i < 2561):
            year.append(i+1)
            i = i + 1
        combo4 = ttk.Combobox(mainFrame,width=5,value = year)
        combo4.place(x=310,y=10)
        #เวลา
        combo5 = ttk.Combobox(mainFrame,width=10)
        combo5.place(x=400,y=10)
        combo5['value'] = ('07.00-08.00','08.00-09.00','09.00-10.00','10.00-11.00','11.00-12.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00','17.00-18.00','18.00-19.00','19.00-20.00','20.00-21.00','21.00-22.00')
        
        boton = Button(mainFrame,text = 'ค้นหา',command = lambda:self.search_list_room(mainFrame,combo1,combo2,combo3,combo4,combo5)).place(x=230,y=50)

        # run
        self.mainloop()

if __name__ == "__main__":
    home()
