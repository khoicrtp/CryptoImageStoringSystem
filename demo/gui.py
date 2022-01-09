import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory
import app
import encrypt
from rsa import create_key_pair

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}
class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, title_styles, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.75)

        def get_signup():
            SignupPage()

        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            # if your want to run the script as it is set validation = True
            global user_auth
            user_auth = app.login(username, password)
            if user_auth==None:
                tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")
            else:
                tk.messagebox.showinfo("Login Successful",
                                       "Welcome {}".format(username))
                root.deiconify()
               
                top.destroy()


class SignupPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#3F6BAA", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        label_user = tk.Label(main_frame, text_styles, text="Your email:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(main_frame, text_styles, text="New Password:")
        label_pw.grid(row=2, column=0)

        label_rsakey = tk.Label(main_frame, text_styles, text="Rsa Key:")
        label_rsakey.grid(row=3, column=0)

        label_e = tk.Label(main_frame, text_styles, text="E:")
        label_e.grid(row=4, column=0)

        label_n = tk.Label(main_frame, text_styles, text="N:")
        label_n.grid(row=5, column=0)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        entry_e = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_e.grid(row=4, column=1)

        entry_n = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_n.grid(row=5, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        button.grid(row=7, column=1)

        def signup():
            # Creates a text file with the Username and password
            user = entry_user.get()
            pw = entry_pw.get()
            e=entry_e.get()
            n=entry_n.get()
            validation = app.signup(user,pw,e,n)
            if validation==0:
                tk.messagebox.showerror("Information", "That Email already exists")
            elif validation==-1:
                tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")
            else:
                tk.messagebox.showinfo("Information", "Sucessfully! Your account details have been stored.")
                SignupPage.destroy(self)
class MenuBar(tk.Menu):
    'contains 2 page Upload and Storage'
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        #to Switch pages
        global top
        top=LoginPage()
        self.add_command(label="Upload", command=lambda: parent.show_frame(uploadPage))
        self.add_command(label="Storage", command=lambda: parent.show_frame(storagePage))

class MyApp(tk.Tk):
    'to control the frames of apps'
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0)
        self.geometry("900x600")
        self.frames = {}
        pages = (uploadPage,storagePage)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(uploadPage)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name): #show selected page from MenuBar 
        frame = self.frames[name]
        frame.tkraise()

class GUI(tk.Frame):
    'Background for each pages'
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
       
class uploadPage(GUI):  # inherits from the GUI class
    'Upload photo page'
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        frame1 = tk.LabelFrame(self, frame_styles, text="Upload photo")
        frame1.place(rely=0.05, relx=0.02, height=400, width=200)

        frame2 = tk.LabelFrame(self, frame_styles, text="Encrypted Image")
        frame2.place(rely=0.05, relx=0.25, height=400, width=650)

        load_bar = tk.Frame(frame1, width=180, height=185)
        load_bar.grid(row=2, column=0, padx=5, pady=5)
        def open_file():
            tk.Label(frame2, text='Uploading Processing...', foreground='blue').grid(row=4, pady=10)
            
            try:
                file_path = askopenfile(mode='r', filetypes=[('Image Files', '.jpg .png .jpge')])
            except:
                tk.messagebox.showerror("Error", "Some thing wrong when choosing photo.")
                return
            if file_path is None:
                return
            
           
            E,N=app.retriveKey(user_auth)
            encrypted=encrypt.encrypt(file_path.name,E,N)
            encrypted=True
            if(encrypted==True):
                size=(650,400)
                try:
                    image=Image.open("encrypted/Encrypted.png")
                except:
                    tk.messagebox.showerror("Error", "Some thing wrong with your photo.")
                    return
                image= image.resize(size,Image.ANTIALIAS)
                photo=ImageTk.PhotoImage(image)
                label= tk.Label(frame2, image=photo)
                label.image= photo
                label.grid(row=0,column=0, )
                app.putdata(user_auth,"encrypted/Encrypted.png","encrypted/key.txt")
                # tk.Label.destroy()
                tk.Label(frame1, text='File Uploaded Successfully!', foreground='green').grid(row=4, pady=10)
            else:
                # tk.Label.destroy()
                tk.Label(frame1, text='File Uploaded Unsuccessfully!', foreground='red').grid(row=4, pady=10)
        upload_img_btn = tk.Button(frame1, text='Upload Photo', command=lambda:open_file())
        upload_img_btn.grid(row=2, column=0)
        
           
    

class storagePage(GUI):
    'Show list of images from firebase'
    def __init__(self, parent, controller):
        
        GUI.__init__(self, parent)
        
        frame1 = tk.LabelFrame(self, frame_styles, text="List")
        frame1.place(rely=0.05, relx=0.02, height=400, width=200)

        frame2 = tk.LabelFrame(self, frame_styles, text="Image")
        frame2.place(rely=0.05, relx=0.25, height=400, width=650)

        scrollbar = tk.Scrollbar(frame1)
        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

        mylist = tk.Listbox(frame1, yscrollcommand = scrollbar.set,width=40 )
        
        # files = app.retriveimages(user_auth) #get all file in storage firebase

        # 'create a list box with all file get above'
        # for file in files: 
        #     mylist.insert(tk.END, file.name) 
        
        'A call back function in mylist.bind. When user choose a file in list box'
        'A image will be downloaded from firebase then show it on frame'
        'A image file will be saved in current project folder'
      
        def callback(event):
            selection = event.widget.curselection()
            value=str(mylist.get(mylist.curselection()))
            print(value)
            index = selection[0]
            data = event.widget.get(index)
            print(data)
            #try:
            app.downloadtoshow(data,user_auth)
            # except:
            #     tk.messagebox.showerror("Error", "Some thing wrong!")
            #     return
            image=Image.open("output.jpg")
            # except:
            #     tk.messagebox.showerror("Error", "Some thing wrong!")
            size=(650,400)
            image= image.resize(size,Image.ANTIALIAS)
            photo=ImageTk.PhotoImage(image)
            label= tk.Label(frame2, image=photo)
            label.image= photo
            label.grid(row=0,column=0, )
        
        mylist.bind('<<ListboxSelect>>',callback)

        'when users press button (btn2). A current image wil be move to a direct path which is selected by user'
        def downloadImage(isAll= False):
            if isAll==False:
                value=str(mylist.get(mylist.curselection()))
                print('s'+value)
                filetype=[('Image Files', '.jpg .png .jpge')]
                try:
                    #open file dialog to get file path to save image
                    # f = asksaveasfile(mode='w',filetypes=filetype, defaultextension=filetype)
                    f=askdirectory()
                except:
                    tk.messagebox.showerror("Error", "Some thing wrong!")
                    return
                if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
                    return
                app.downloadImage(user_auth,value,f)
                # im = Image.open("output.jpg") #get current image
                # if im.mode != "RGB":
                #     im = im.convert("RGB")
                # im.save(f) #save it to path f
            else:
                f=askdirectory()
                app.downloadAll(f)
            
       
        btn2 = tk.Button(frame1, text='Download Image', command= lambda: downloadImage())
        btn2.pack(side="bottom")
        btn3 = tk.Button(frame1, text='Download All Image', command= lambda: downloadImage(isAll=True))
        btn3.pack(side="bottom")

        'functions to refresh list box. When user upload a photo from uploadPage '
        'They need to press Refresh button to update new photo to GUI'
        def LoadList():
            self.files = app.retriveimages(user_auth)
            for file in self.files:
                if 'key' in file: continue
                mylist.insert(tk.END, file.split('/')[-1])
        def Refresh_data():
            # Deletes the data in the current listbox and reinserts it.
            mylist.delete(0,tk.END)  
            LoadList()

        button2 = ttk.Button(frame1, text="Refresh", command=lambda: Refresh_data())
        button2.pack(side="bottom")

        mylist.pack( side = tk.LEFT, fill = tk.BOTH )
        scrollbar.config( command = mylist.yview )

#main

root=MyApp()
root.withdraw()
root.title("Tkinter App Template")
root.mainloop()
