import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory
import app 

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}


class MenuBar(tk.Menu):
    'contains 2 page Upload and Storage'
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        #to Switch pages
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
        upload_img_btn = ttk.Button(frame1, text='Upload Photo', command=lambda:open_file())
        upload_img_btn.grid(row=2, column=0)
        def open_file():
            try:
                file_path = askopenfile(mode='r', filetypes=[('Image Files', '.jpg .png .jpge')])
            except:
                tk.messagebox.showerror("Error", "Some thing wrong when choosing photo.")
                return
            if file_path is None:
                return
            try:
                image=Image.open(file_path.name)
            except:
                tk.messagebox.showerror("Error", "Some thing wrong with your photo.")
                return
            size=(650,400)
            image= image.resize(size,Image.ANTIALIAS)
            photo=ImageTk.PhotoImage(image)

            'encrypted image'
            'to do: Not done yet'

            label= tk.Label(frame2, image=photo)
            label.image= photo
            label.grid(row=0,column=0, )
            app.putimage(file_path.name)
            tk.Label(frame1, text='File Uploaded Successfully!', foreground='green').grid(row=4, pady=10)
           
    

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
        
        self.files = app.retriveimages() #get all file in storage firebase

        'create a list box with all file get above'
        for file in self.files: 
            mylist.insert(tk.END, file.name) 
        
        'A call back function in mylist.bind. When user choose a file in list box'
        'A image will be downloaded from firebase then show it on frame'
        'A image file will be saved in current project folder'
        def callback(event):
            selection = event.widget.curselection()
            index = selection[0]
            data = event.widget.get(index)
            try:
                app.downloadtoshow(data)
                image=Image.open("output.jpg")
            except:
                tk.messagebox.showerror("Error", "Some thing wrong!")
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
                filetype=[('Image Files', '.jpg .png .jpge')]
                try:
                    #open file dialog to get file path to save image
                    f = asksaveasfile(mode='w',filetypes=filetype, defaultextension=filetype)
                except:
                    tk.messagebox.showerror("Error", "Some thing wrong!")
                if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
                    return
                im = Image.open("output.jpg") #get current image
                if im.mode != "RGB":
                    im = im.convert("RGB")
                im.save(f) #save it to path f
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
            self.files = app.retriveimages()
            for file in self.files:
                mylist.insert(tk.END, file.name)
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
root.mainloop()