
from tkinter import *
import tkinter.messagebox as tm
from tkinter import *
from tkinter import ttk
import api
import json
A = api.API_cen()

class login(Tk):

    def __init__(self):
        Tk.__init__(self)
        frame=Frame(self)


        self.notebook = ttk.Notebook(frame)


        self.login_frame = Frame(frame, padx=100, pady=100)
        Label(self.login_frame, text="LOG IN\n").grid(row=0, column=1, sticky=W)
        Label(self.login_frame, text="Username").grid(row=1, sticky=E)
        Label(self.login_frame, text="Password").grid(row=2, sticky=E)
        self.entry_username = Entry(self.login_frame)
        self.entry_username.grid(row=1, column=1)
        self.entry_password = Entry(self.login_frame, show="*")
        self.entry_password.grid(row=2, column=1)
        Checkbutton(self.login_frame, text="Keep me logged in").grid(columnspan=2)
        Button(self.login_frame, text="Login",command=self._login_btn_clicked).grid(row=4,column=0,columnspan=2)

        self.signup_frame = Frame(frame,padx=100,pady=100)
        Label(self.signup_frame, text="SIGN UP\n").grid(row=0, column=0, sticky=W)
        Label(self.signup_frame, text="New Username: ").grid(row=1, column=0, sticky=W)
        Label(self.signup_frame, text="New Password: ").grid(row=2, column=0, sticky=W)
        self.entry_usernames = Entry(self.signup_frame)
        self.entry_usernames.grid(row=1, column=1)
        self.entry_passwords = Entry(self.signup_frame, show='*')
        self.entry_passwords.grid(row=2, column=1)
        Button(self.signup_frame, text="Signup",command=self._register_btn_clicked).grid(row=4,column=0,columnspan=2)



        self.notebook.add(self.login_frame, text="login")
        self.notebook.add(self.signup_frame, text="sign up")

        self.notebook.pack()
        frame.pack()
        self.mainloop()

    def _register_btn_clicked(self):
        username = self.entry_usernames.get()
        password = self.entry_passwords.get()
        
        status = self.regischeck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Regis info", "Done")
        else:
            tm.showerror("Regis error", status)
    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)
        status = self.logincheck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Login info", "Welcome")
            self.destroy()
        else:
            tm.showerror("Login error", status)
        

    def regischeck(self,username,password):
        respond = json.loads(A.SendRegister(username,password))
        if respond['status']=="sucess":
            return True
        return respond['error']

    def logincheck(self,username,password):
        resopod = json.loads(A.SendLogin(username,password))
        if resopod['status']=="sucess":
            return True
        return resopod['error']

if __name__ == "__main__":
    login()
