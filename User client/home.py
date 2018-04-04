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
        menuList = Frame(self, relief=SUNKEN)
        mainFrame = Frame(self,width=500, height=400, bd=1, relief=SUNKEN)
        Button(menuList, text='จองห้อง',relief="flat",padx=39).pack(side=TOP, padx=5)
        Button(menuList, text='ตรวจสอบห้องว่าง',relief="flat",padx=19,command=lambda:cancelnaja(mainFrame,self)).pack(side=TOP, padx=5)
        Button(menuList, text='ตารางการใช้ห้อง',relief="flat",padx=20).pack(side=TOP, padx=5)
        menuList.pack( side=LEFT,fill=Y,pady=10, padx=5)
        mainFrame.pack(side=LEFT,expand=1, pady=10, padx=5)
        # run
        #Button(mainFrame, text='จองห้อง',relief="flat",padx=39).pack(side=TOP, padx=5)
        self.mainloop()

if __name__ == "__main__":
    home()








#def cancelnaja() :
 #   print("CencelNa")
