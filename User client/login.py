from tkinter import *
import tkinter.messagebox as tm
from tkinter import *
from tkinter import ttk
import api

def post_login(login):
    #respond = {"status":"fail","error":login['username']+login['password']}
    A=api.getipfromfile("config.txt")
    respond = api.SendLogin(login['username'],api.hash_password(login['password']),A)
    print(respond)
    return respond

def post_regis(login):
    # respond = {"status":"fail","error":login['username']+login['password']}
    A=api.getipfromfile("config.txt")
    respond = api.SendRegister(login['username'],api.hash_password(login['password']),A)
    print(respond)
    return respond

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
        Button(self.login_frame, text="Login",command=self._login_btn_clicked()).grid(row=4,column=0,columnspan=2)

        self.signup_frame = Frame(frame,padx=100,pady=100)
        Label(self.signup_frame, text="SIGN UP\n").grid(row=0, column=0, sticky=W)
        Label(self.signup_frame, text="New Username: ").grid(row=1, column=0, sticky=W)
        Label(self.signup_frame, text="New Password: ").grid(row=2, column=0, sticky=W)
        Entry(self.signup_frame).grid(row=1, column=1)
        Entry(self.signup_frame, show='*').grid(row=2, column=1)
        Button(self.signup_frame, text="Signup").grid(row=4,column=0,columnspan=2)



        self.notebook.add(self.login_frame, text="login")
        self.notebook.add(self.signup_frame, text="sign up")

        self.notebook.pack()
        frame.pack()
        self.mainloop()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.logincheck(username,password)

        # print(username, password)
        status = self.logincheck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Login info", "Welcome")
        else:
            tm.showerror("Login error", status)

    def regischeck(self,username,password):
        regis = { }
        regis["username"] = username
        regis["password"] = password
        #response = post_regis(regis)
        #if(response['status']=="success"):
        #    return True
        #else:
        #    return response['error']

    def logincheck(self,username,password):
        login = { }
        login["username"] = username
        login["password"] = password
        #response = post_login(login)
        #if(response['status']=="sucess"):
         #   root.destroy
          #  return True
        #else:
         #   return response['error']

if __name__ == "__main__":
    login()
