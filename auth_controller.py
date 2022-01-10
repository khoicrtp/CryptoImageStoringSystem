import requests
import json

BASE="https://test-eflask-crypto.herokuapp.com/"

def login_verify(user,pw):
    json_data = json.dumps({'username':user,'password':pw})
    response = requests.post(BASE+'/users/login',json=json_data)
    if(response.status_code==200):
        # print(response.json())
        return True#, None #,response.json()
    elif(response.status_code==404):
        return False, None
    
def register_user(user,pw,n,e):
    json_data = json.dumps({'username':user,'password':pw,'n_publickey':n,'e_publickey':e})
    response = requests.post(BASE+'/users/register',json=json_data)
    if(response.status_code==200):
        return True
    elif(response.status_code==404):
        return False
    
    