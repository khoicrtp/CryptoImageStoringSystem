from tkinter import *

def login():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("Fill the empty field!!!")
    else:
      if uname=="abcd@gmail.com" and pwd=="abc123":
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global  message
    global username
    global password
    global login_screen
    login_screen = Tk()
    username = StringVar()
    password = StringVar()
    message=StringVar()
    login_screen.title("Crypto Images System")
    login_screen.geometry("300x250")
    Label(login_screen,width="300", text="Please enter your account below", bg="blue",fg="white").pack()
    Label(login_screen, text="Username  ").place(x=20,y=40)
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    Label(login_screen, text="Password  ").place(x=20,y=80)
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    Label(login_screen, text="",textvariable=message).place(x=90,y=100)
    Button(login_screen, text="Login", width=10, height=1, bg="blue",command=login).place(x=40,y=130)
    Button(login_screen, text="Register", width=10, height=1, bg="blue",command=login).place(x=160,y=130)
    login_screen.mainloop()

Loginform()