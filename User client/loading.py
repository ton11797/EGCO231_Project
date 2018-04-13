<<<<<<< HEAD
from tkinter import *

import os


class loading(Tk):
    def __init__(self):
        #set geometry
        width_ofwindow=600
        height_ofwindow=300
        Tk.__init__(self)
        frame=Frame(self)
        self.overrideredirect(1)
        screenwidth=self.winfo_screenheight()
        screenheight=self.winfo_screenheight()
        x_coordinate=(screenwidth/2)
        y_coordinate=(screenheight/2)-(height_ofwindow/2)
        self.wm_geometry("%dx%d+%d+%d"%(width_ofwindow,height_ofwindow,x_coordinate,y_coordinate))

        #Load image
        Photo=PhotoImage(file='data/1.png')
        label=Label(frame,width=600, height=300,image=Photo)
        label.image = Photo
        label.pack()
        frame.pack()

        # run this after 3 secs
        self.after(3000,self.close)
        self.mainloop()

    def close(self):
        self.destroy()




if __name__ == "__main__":
    loading()
=======
from tkinter import *

import os


class loading(Tk):
    def __init__(self):
        #set geometry
        width_ofwindow=600
        height_ofwindow=300
        Tk.__init__(self)
        frame=Frame(self)
        self.overrideredirect(1)
        screenwidth=self.winfo_screenheight()
        screenheight=self.winfo_screenheight()
        x_coordinate=(screenwidth/2)
        y_coordinate=(screenheight/2)-(height_ofwindow/2)
        self.wm_geometry("%dx%d+%d+%d"%(width_ofwindow,height_ofwindow,x_coordinate,y_coordinate))

        #Load image
        Photo=PhotoImage(file='data/1.png')
        label=Label(frame,width=600, height=300,image=Photo)
        label.image = Photo
        label.pack()
        frame.pack()

        # run this after 3 secs
        self.after(3000,self.close)
        self.mainloop()

    def close(self):
        self.destroy()




if __name__ == "__main__":
    loading()
>>>>>>> Book
