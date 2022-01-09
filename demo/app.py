import pyrebase
from PIL import Image
import time
import re
# firebaseConfig = {
#   "apiKey": "AIzaSyCzj3cwI4Hxwgk2vbGolw4xDMBDksm1_ew",
#   "authDomain": "pyrebase-b0a70.firebaseapp.com",
#   "databaseURL": "https://pyrebase-b0a70-default-rtdb.firebaseio.com",
#   "projectId": "pyrebase-b0a70",
#   "storageBucket": "pyrebase-b0a70.appspot.com",
#   "messagingSenderId": "423079629827",
#   "appId": "1:423079629827:web:53bc0d781cc2150e51aa36",
#   "measurementId": "G-BLLVVH9Z59",
#   "serviceAccount": "pyrebase-b0a70-firebase-adminsdk-4nyz0-5ce7664c34.json"
# }
firebaseConfig = {
  'apiKey': "AIzaSyCrE2-NwCRX_aYNqWLO2vccndLsjFKpI6k",
  'authDomain': "cryptoimagesystem.firebaseapp.com",
  'databaseURL': "https://cryptoimagesystem-default-rtdb.firebaseio.com",
  'projectId': "cryptoimagesystem",
  'storageBucket': "cryptoimagesystem.appspot.com",
  'messagingSenderId': "116703538213",
  'appId': "1:116703538213:web:0f4e675d3d7ed62133a3cc",
  'measurementId': "G-4RQGMEBKYV",
  "serviceAccount": "cryptoimagesystem-firebase-adminsdk-5cvrj-849cae63bd.json"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()
storage = firebase.storage()
def signup(email,passw,e,n):
  try:
    if(len(passw)<6):
      return -1
    user=auth.create_user_with_email_and_password(email, passw)
    data={'E':e,'N':n}
    db.child('users').child(user['localId']).child('RSA').set(data)
    return 1
  except:
    return 0

def login(email,passw):
  try:
    user=auth.sign_in_with_email_and_password(email,passw)
    return user
  except:
    return None
    


def putdata(user,imagepath,keypath):
  timestr = time.strftime("%Y%m%d-%H%M%S")
  storage.child("users").child(user['localId']).child("images/"+timestr).put(imagepath)
  storage.child("users").child(user['localId']).child("key/"+timestr).put(keypath)

def retriveKey(user):
  values=dict(db.child('users').child(user['localId']).child('RSA').get().val())
  E=values['E']
  N=values['N']
  return int(E),int(N)

def retriveimages(user):
  files=storage.child('users/'+user['localId']+'/images/').list_files()
  res=[]
  for file in files:
    if user['localId'] in file.name:
      res.append(file.name)
  return res

def downloadtoshow(filestoragename,user):
    storage.child('users/'+user['localId']+'/images/'+filestoragename).download("output.jpg")

def downloadImage(user,filestoragename,outputpath):
    storage.child('users/'+user['localId']+'/images/'+filestoragename).download(outputpath+'/'+filestoragename+'.png')
    storage.child('users/'+user['localId']+'/key/'+filestoragename).download(outputpath+'/'+filestoragename+'.txt')
    
# def downloadImage(filestoragename,url):
#   try:
#     storage.child(filestoragename).download(url)
#   except:
#     print("None")

def downloadAll(filepath):
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
      
