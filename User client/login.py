from tkinter import *
import tkinter.messagebox as tm

class login(Tk):
    def __init__(self):
        # Init
        Tk.__init__(self)
        self.winfo_toplevel().title("Login")
        # Login frame
        login_frame = Frame(self, height = 165, width = 420,padx=20,pady=50, relief = FLAT, bd = 1)
        login_frame.grid()
        
        login_frame.label_title = Label(login_frame, text="LOG IN\n")
        login_frame.label_title.grid(row=0, column=1, sticky=W)
        
        login_frame.label_username = Label(login_frame, text="Username")
        login_frame.label_password = Label(login_frame, text="Password")

        login_frame.entry_username = Entry(login_frame)
        login_frame.entry_password = Entry(login_frame, show="*")

        login_frame.label_username.grid(row=1, sticky=E)
        login_frame.label_password.grid(row=2, sticky=E)
        login_frame.entry_username.grid(row=1, column=1)
        login_frame.entry_password.grid(row=2, column=1)

        login_frame.checkbox = Checkbutton(login_frame, text="Keep me logged in")
        login_frame.checkbox.grid(columnspan=2)

        login_frame.logbtn = Button(login_frame, text="Login", command=(lambda: loginCheck(self)))
        login_frame.logbtn.grid(row=4,column=0)

        login_frame.logbtn = Button(login_frame, text="Sign up", command=self._signup_btn_clicked)
        login_frame.logbtn.grid(row=4,column=1)


        self.grid()
        # run
        self.mainloop()

    def loginCheck(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "fon" and password == "password":
            tm.showinfo("Login info", "Welcome Fon")
        else:
            tm.showerror("Login error", "Incorrect username")

        self.destroy()
        
    def _signup_btn_clicked(self):
        # print("Clicked")
        #self.destroy()
        self = Tk()
        
        self.frame = Frame(self,padx=100,pady=100)
        self.frame.grid()
        
        self.label_title = Label(self.frame, text="SIGN UP\n")
        self.label_title.grid(row=0, column=0, sticky=W)
 
        self.label_newusername = Label(self.frame, text="New Username: ")
        self.label_newpassword = Label(self.frame, text="New Password: ")
        self.label_newusername.grid(row=1, column=0, sticky=W)
        self.label_newpassword.grid(row=2, column=0, sticky=W)
 
        self.entry_newusername = Entry(self.frame)
        self.entry_newpassword = Entry(self.frame, show='*')
        self.entry_newusername.grid(row=1, column=1)
        self.entry_newpassword.grid(row=2, column=1)
 
        self.signbtn = Button(self.frame, text="Signup",command = self.destroy)
        self.signbtn.grid(columnspan=3, sticky=W)

        self.mainloop()
        

if __name__ == "__main__":
    login()
