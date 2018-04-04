from tkinter import *
from tkinter import ttk
class home(Tk):
    def __init__(self):
        Tk.__init__(self)
        menuList = Frame(self, relief=SUNKEN)
        mainFrame = Frame(self,width=500, height=400, bd=1, relief=SUNKEN)
        
        Button(menuList, text='จองห้อง',relief="flat",padx=39).pack(side=TOP, padx=5)
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19,command = lamdba:self.search_room(mainFrame)).pack(side=TOP, padx=5)
        Button(menuList, text='ตารางการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5)
        menuList.pack( side=LEFT,fill=Y,pady=10, padx=5)
        mainFrame.pack(side=LEFT,expand=1, pady=10, padx=5)

    def search_room(self,mainFrame):
        label = Label(mainFrame,text ="ห้อง : ")
        label.place(x=5,y=10)
        label = Label(mainFrame,text ="วัน : ")
        label.place(x=85,y=10)
        label = Label(mainFrame,text ="เดือน : ")
        label.place(x=155,y=10)
        label = Label(mainFrame,text ="ปี : ")
        label.place(x=255,y=10)
        label = Label(mainFrame,text ="เวลา : ")
        label.place(x=305,y=10)
        #ห้อง
        combo1 = ttk.Combobox(mainFrame,width=5)
        combo1.place(x=28,y=10)
        combo1['value'] = ('R321')
        #วัน
        combo2 = ttk.Combobox(mainFrame,width=5)
        combo2.place(x=95,y=50)
        combo2['value'] = ('1','','','','','','','','','','','','','','','','','','','','','','','','','','')
        
        #for i in 32:
        #    combo2['value'] = i
        
        #เดือน
        combo3 = ttk.Combobox(mainFrame,width=10)
        combo3.place(x=265,y=10)
        combo3['value'] = ('มกราคม','กุมพาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม')
        #ปี
        combo3 = ttk.Combobox(mainFrame,width=5)
        combo3.place(x=285,y=5)
        combo3['value'] = ('2559','2560','2561','2562','2563','2564','2565','2566','2567')
        #เวลา
        combo4 = ttk.Combobox(mainFrame,width=10)
        combo4.place(x=340,y=10)
        combo4['value'] = ('07.00-08.00','08.00-09.00','09.00-10.00','10.00-11.00','11.00-12.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00','17.00-18.00','18.00-19.00','19.00-20.00','20.00-21.00','21.00-22.00')
        

        
        # run
        self.mainloop()

if __name__ == "__main__":
    home()
