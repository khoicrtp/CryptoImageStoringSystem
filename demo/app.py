import pyrebase
from PIL import Image
import time
import re
firebaseConfig = {
  "apiKey": "AIzaSyCzj3cwI4Hxwgk2vbGolw4xDMBDksm1_ew",
  "authDomain": "pyrebase-b0a70.firebaseapp.com",
  "databaseURL": "https://pyrebase-b0a70-default-rtdb.firebaseio.com",
  "projectId": "pyrebase-b0a70",
  "storageBucket": "pyrebase-b0a70.appspot.com",
  "messagingSenderId": "423079629827",
  "appId": "1:423079629827:web:53bc0d781cc2150e51aa36",
  "measurementId": "G-BLLVVH9Z59",
  "serviceAccount": "pyrebase-b0a70-firebase-adminsdk-4nyz0-5ce7664c34.json"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()
def putimage(filepath):
  timestr = time.strftime("%Y%m%d-%H%M%S")
  storage = firebase.storage()
  # as admin
  storage.child("images/"+timestr).put(filepath)

def retriveimages():
  firebase = pyrebase.initialize_app(firebaseConfig)
  storage = firebase.storage()
  files=storage.list_files()
  return files

def downloadtoshow(filestoragename):
  firebase = pyrebase.initialize_app(firebaseConfig)
  storage = firebase.storage()
  try:
    storage.child(filestoragename).download("output.jpg")
  except:
    print("None")

def downloadAll(filepath):
  print(filepath)
  firebase = pyrebase.initialize_app(firebaseConfig)
  storage = firebase.storage()
  files=storage.list_files()
  ab=str(1) 
  for file in files:
    try:
      # print(file.name)
      storage.child(file.name).download(filepath+"/"+ab+".jpg")
      x=int(ab)     
      ab=str(x+1)
    except:
      print('Download Failed') 
    
