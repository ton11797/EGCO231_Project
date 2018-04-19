<<<<<<< HEAD
from tkinter import *
import tkinter.messagebox as tm
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

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.frame = Frame(self,padx=100,pady=100)
        self.frame.pack()

        self.label_title = Label(self.frame, text="LOG IN\n")
        self.label_title.grid(row=0, column=1, sticky=W)
        
        self.label_username = Label(self.frame, text="Username")
        self.label_password = Label(self.frame, text="Password")

        self.entry_username = Entry(self.frame)
        self.entry_password = Entry(self.frame, show="*")

        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=2, sticky=E)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        self.checkbox = Checkbutton(self.frame, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self.frame, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=4,column=0)

        self.logbtn = Button(self.frame, text="Sign up", command=self._signup_btn_clicked)
        self.logbtn.grid(row=4,column=1)


        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.logincheck(username,password)

        # print(username, password)
        status = self.logincheck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Login info", "Welcome Fon")
        else:
            tm.showerror("Login error", status)
            
    def _add_signup_btn_clicked(self):
        # print("Clicked")
        username = self.entry_newusername.get()
        password = self.entry_newpassword.get()

        self.regischeck(username,password)

        # print(username, password)
        status = self.regischeck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Sign Up info", "Welcome :)")
        else:
            tm.showerror("Sign Up error", status)


    def _signup_btn_clicked(self):
        # print("Clicked")
        self.frame.destroy()

        self.frame = Frame(self,padx=100,pady=100)
        self.frame.pack()
        
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
 
        self.signbtn = Button(self.frame, text="Signup",command = self._add_signup_btn_clicked)
        self.signbtn.grid(columnspan=3, sticky=W)
                              
        self.pack()
        
    def regischeck(self,username,password):
        regis = { }
        regis["username"] = username
        regis["password"] = password 
        response = post_regis(regis)
        print(response)
        if(response['status']=="success"):
            # root.destroy
            return True
        else:
            return response['error']

    def logincheck(self,username,password):
        login = { }
        login["username"] = username
        login["password"] = password
        response = post_login(login)
        print(response)
        if(response['status']=="success"):
            root.destroy
            return True
        else:
            return response['error']



root = Tk()
lf = LoginFrame(root)
root.mainloop()
=======
from tkinter import *
import tkinter.messagebox as tm

def post_login(login):
    #respond = {"status":"fail","error":login['username']+login['password']}

    respond = {"status":"success","error":login['username']+login['password']}
    return respond

def post_regis(login):
    respond = {"status":"fail","error":login['username']+login['password']}
    #respond = {"status":"success","error":login['username']+login['password']}
    return respond

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.frame = Frame(self,padx=100,pady=100)
        self.frame.pack()

        self.label_title = Label(self.frame, text="LOG IN\n")
        self.label_title.grid(row=0, column=1, sticky=W)
        
        self.label_username = Label(self.frame, text="Username")
        self.label_password = Label(self.frame, text="Password")

        self.entry_username = Entry(self.frame)
        self.entry_password = Entry(self.frame, show="*")

        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=2, sticky=E)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        self.checkbox = Checkbutton(self.frame, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self.frame, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row=4,column=0)

        self.logbtn = Button(self.frame, text="Sign up", command=self._signup_btn_clicked)
        self.logbtn.grid(row=4,column=1)


        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.logincheck(username,password)

        # print(username, password)
        status = self.logincheck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Login info", "Welcome Fon")
        else:
            tm.showerror("Login error", status)
            
    def _add_signup_btn_clicked(self):
        # print("Clicked")
        username = self.entry_newusername.get()
        password = self.entry_newpassword.get()

        self.regischeck(username,password)

        # print(username, password)
        status = self.regischeck(username,password)
        print(status)
        if (status==True):
            tm.showinfo("Sign Up info", "Welcome :)")
        else:
            tm.showerror("Sign Up error", status)


    def _signup_btn_clicked(self):
        # print("Clicked")
        self.frame.destroy()

        self.frame = Frame(self,padx=100,pady=100)
        self.frame.pack()
        
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
 
        self.signbtn = Button(self.frame, text="Signup",command = self._add_signup_btn_clicked)
        self.signbtn.grid(columnspan=3, sticky=W)
                              
        self.pack()
        
    def regischeck(self,username,password):
        regis = { }
        regis["username"] = username
        regis["password"] = password 
        response = post_regis(regis)
        print(response)
        if(response['status']=="success"):
            #root.destroy
            return True
        else:
            return response['error']

    def logincheck(self,username,password):
        login = { }
        login["username"] = username
        login["password"] = password
        response = post_login(login)
        print(response)
        if(response['status']=="success"):
            root.destroy
            return True
        else:
            return response['error']



root = Tk()
lf = LoginFrame(root)
root.mainloop()
>>>>>>> Book
