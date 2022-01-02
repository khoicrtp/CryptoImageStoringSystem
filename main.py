import pyrebase
import mysql.connector
import os


#mysql://ba210f51bd8223:9bc50fbc@us-cdbr-east-05.cleardb.net/heroku_d08923bbc460fa4?reconnect=true
mydb = mysql.connector.connect(
  host="us-cdbr-east-05.cleardb.net",
  user="ba210f51bd8223",
  password="9bc50fbc",
  database="heroku_d08923bbc460fa4"
)
mycursor = mydb.cursor()

def insertUser(username, password, publickey): 
  sql = "INSERT INTO ACCOUNT (USERNAME, PASSWORD, PUBLICKEY) VALUES (%s, %s, %s);"
  val = (username, password, publickey)
  mycursor.execute(sql, val)
  mydb.commit()

def selectAll():
  sql = "SELECT * FROM ACCOUNT;"
  #val = (username, password)
  mycursor.execute(sql)
  res = mycursor.fetchall()
  return res

userID={"username": "UOa2", "password": "abc", "key":"1234"}
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

#insertUser("UOa2", "a2")
print(selectAll())
