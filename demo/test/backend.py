import requests
import json
import base64
import rsacrypto
import numpy as np
from PIL import Image
import time
import os
BASE="https://test-eflask-crypto.herokuapp.com/"

def makedir(user):
    if not os.path.exists(user):
            os.makedirs(user+'/encrypted')
            os.makedirs(user+'/images')
            os.makedirs(user+'/npy')
def login_verify(user,pw):
    json_data = json.dumps({'username':user,'password':pw})
    response = requests.post(BASE+'users/login',json=json_data)
    if(response.status_code==200):
        # print(response.json())
        return True#, None #,response.json()
    elif(response.status_code==404):
        return False#, None
    
def register_user(user,pw,n,e):
    json_data = json.dumps({'username':user,'password':pw,'n_publickey':n,'e_publickey':e})
    response = requests.post(BASE+'users/register',json=json_data)
    if(response.status_code==200):
        return True
    elif(response.status_code==404):
        return False
    
def register_user(user,pw,n,e):
    json_data = json.dumps({'username':user,'password':pw,'n_publickey':n,'e_publickey':e})
    response = requests.post(BASE+'/users/register',json=json_data)
    if(response.status_code==200):
        return True
    elif(response.status_code==404):
        return False
    
    
def getKey(username):
    x = requests.get(BASE+'/'+username)
    if(x.status_code==200):
        data=dict(x.json())
        E=data['e_publickey']
        N=data['n_publickey']
        return True,E,N
    elif(x.status_code==404):
        return False
def postImgae(img,username):
    
    timestr = time.strftime("%Y%m%d%H%M%S")
    makedir(username)
    data = np.asarray(img)
    #_,e,n=getKey(username)
    enc_img, enc = rsacrypto.encrypt(data, 13, 899)

    image1 = Image.fromarray(enc_img, 'RGB')
    image1 = image1.save(username+"/encrypted/"+timestr+".png")
    np.save(username+"/npy/"+timestr+".npy", enc)
    files = {
    'file': open(username+"/npy/"+timestr+".npy", "rb"),
    }
    response = requests.post(BASE+username+'/'+timestr+'.png/',files=files)
    print(response.status_code)
    if(response.status_code==200):
        return True
    elif(response.status_code==404):
        return False

def getImage(url,username):
    x = requests.get(BASE+'/'+username)
    None
def retriveimages(username):
    x = requests.get(BASE+'/'+username+'/images_list')
    if(x.status_code==200):
        data=dict(x.json())
        values=data['names']
        files=[]
        for val in values:
            files.append(val[0])
        return True,files
    elif(x.status_code==404):
        return False

def downloadAImage(username,url):

    None
