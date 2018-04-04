from tkinter import *
from tkinter import Tk, StringVar, ttk
class home(Tk):
    def __init__(self):
        Tk.__init__(self)
        menuList = Frame(self, relief=SUNKEN)
        Button(menuList, text='จองห้อง',relief="flat",padx=39,command=(lambda:self.book(mainFrame))).pack(side=TOP, padx=5)
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19).pack(side=TOP, padx=5)
        Button(menuList, text='ตารางการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5)
        menuList.pack( side=LEFT,fill=Y,pady=10, padx=5)
        mainFrame = Frame(self,width=500, height=400, bd=1, relief=SUNKEN)
        mainFrame.pack(side=LEFT,expand=1, pady=10, padx=5)     
        # run
        self.mainloop()

    def book(self,mainFrame):
        nameRoom = Label(mainFrame,text="เลือกห้องประชุม")
        nameRoom.place(x=50,y=10)
        combo = ttk.Combobox(mainFrame)
        combo.place(x=50,y=30)
        combo['values'] = ('15','17','6','0')
        combo.current(3)
        mainFrame.mainloop()

if __name__ == "__main__":
    home()
