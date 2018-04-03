from tkinter import *

class login(Tk):
    def __init__(self):
        # Init
        Tk.__init__(self)
        self.winfo_toplevel().title("Login")
        # Login frame
        login_frame = Frame(self, height = 165, width = 420,padx=20,pady=50, relief = FLAT, bd = 1)
        login_frame.grid()
        Button(login_frame, text ="Login",command=(lambda: self.loginCheck())).grid(column=0,row=0)
        # run
        self.mainloop()

    def loginCheck(self):
        self.destroy()

if __name__ == "__main__":
    login()