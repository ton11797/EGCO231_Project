from tkinter import *
from tkinter import Tk, StringVar, ttk
import json
import pickme

class home(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        menuList = Frame(self, relief=SUNKEN)
        Button(menuList, text='จองห้อง',relief="flat",padx=39,command=(lambda:self.pickme.book(mainFrame))).pack(side=TOP, padx=5)
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19).pack(side=TOP, padx=5)
        Button(menuList, text='ตารางการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5)
        menuList.pack( side=LEFT,fill=Y,pady=10, padx=5)
        mainFrame = Frame(self,width=500, height=400, bd=1, relief=SUNKEN)
        mainFrame.pack(side=LEFT,expand=1, pady=10, padx=5)     
        # run
        self.mainloop()

    def book(self,mainFrame):
        textRoom = Label(mainFrame,text="เลือกห้องประชุม")
        textRoom.place(x=80,y=20)
        combo = ttk.Combobox(mainFrame)
        combo.place(x=80,y=50)
        combo['values'] = ('15','17','6','0')

        textDate = Label(mainFrame,text="เลือกวัน")
        textDate.place(x=280,y=20)
        combo = ttk.Combobox(mainFrame)
        combo.place(x=280,y=50)
        combo['values'] = ('15','17','6','0')

        textTime1 = Label(mainFrame,text="เวลาเริ่มต้น")
        textTime1.place(x=80,y=100)
        combo = ttk.Combobox(mainFrame)
        combo.place(x=80,y=130)
        combo['values'] = ('15','17','6','0')

        textTime2 = Label(mainFrame,text="เวลาสิ้นสุด")
        textTime2.place(x=280,y=100)
        combo = ttk.Combobox(mainFrame)
        combo.place(x=280,y=130)
        combo['values'] = ('15','17','6','0')

        textName = Label(mainFrame,text="ชื่อนาสกุลผู้จอง")
        textName.place(x=80,y=180)
        combo = ttk.Entry(mainFrame)
        combo.place(x=80,y=210)
        
        

        textOption = Label(mainFrame,text="อุปกรณ์ที่ใช้")
        textOption.place(x=80,y=250)
        R1 = ttk.Radiobutton(mainFrame, text="โปรเจตเตอร์",value=1).place(x=80,y=280)
        R2 = ttk.Radiobutton(mainFrame, text="คอมพิวเตอร์",value=2).place(x=170,y=280)
        R3 = ttk.Radiobutton(mainFrame, text="ไมโครโฟน",value=3).place(x=260,y=280)

        b1 = ttk.Button(mainFrame,text='ยืนยัน',command=(lambda:self.check(mainFrame))).place(x=80,y=330)
        b2 = ttk.Button(mainFrame,text='ล้างข้อมูล').place(x=180,y=330)
        
        mainFrame.mainloop()

    def pickRoom(self,mainFrame):
        a=Pickme()
        a.book()

    def check(self,mainFrame):
        data = {
            "NAME":""
        }
        jsonData = json.dumps(data)
        print(jsonData)
        with open('JSONDATA.json','w') as f:
            json.dump(jsonData,f)
        mainFrame.mainloop()

if __name__ == "__main__":
    home()
