from tkinter import * 
class home(Tk): 
    def __init__(self): 
        Tk.__init__(self) 
        menuList = Frame(self, relief=SUNKEN) 
        Button(menuList, text='จองห้อง',relief="flat",padx=39).pack(side=TOP, padx=5) 
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19).pack(side=TOP, padx=5) 
        Button(menuList, text='ตารางการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5)
        Button(menuList, text='ยกเลิกการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5) 
        menuList.pack( side=LEFT,fill=Y,pady=10, padx=5) 
        mainFrame = Frame(self,width=500, height=400, bd=1, relief=SUNKEN) 
        mainFrame.pack(side=LEFT,expand=1, pady=10, padx=5) 
        # run 
        self.mainloop() 
 
if __name__ == "__main__": 
    home()
