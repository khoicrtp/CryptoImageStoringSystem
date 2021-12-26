import pyrebase
import os

userID={"username": "UOa2", "password": "abc"}
path = userID["username"]+"/"
firebaseConfig = {
  "apiKey": "AIzaSyCrE2-NwCRX_aYNqWLO2vccndLsjFKpI6k",
  "authDomain": "cryptoimagesystem.firebaseapp.com",
  "projectId": "cryptoimagesystem",
  "storageBucket": "cryptoimagesystem.appspot.com",
  "databaseURL": "cryptoimagesystem.appspot.com",
  "messagingSenderId": "116703538213",
  "appId": "1:116703538213:web:0f4e675d3d7ed62133a3cc",
  "measurementId": "G-4RQGMEBKYV",
  "serviceAccount": "serviceKey.json"
};

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage=firebase_storage.storage()

def uploadImage(filename):
  storage.child(userID["username"]+"/"+filename).put(filename)

def downloadImage(filename):
  storage.child(userID["username"]+"/"+filename).download(userID["username"]+"/"+filename)

uploadImage("3h.jpg")

allFiles=storage.list_files()
#downloadImage("3h.jpg")
for file in allFiles:
  print(file)
  if(os.path.exists(path)==False):
    os.mkdir(path)
  storage.child(file.name).download(file.name)
