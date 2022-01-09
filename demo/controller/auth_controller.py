import requests
BASE="http://localhost:5000"

def login_verify(user,pw):
    json_data = {'username':user,'password':pw}
    response = requests.post(BASE+'/users/login',data=json_data)
    if(response.status_code==500):
        return True,response.json()
    elif(response.status_code==404):
        return False, None
    
def register_user(user,pw,n,e):
    json_data = {'username':user,'password':pw,'n_publickey':n,'e_publickey':e}
    response = requests.post(BASE+'/users/register',data=json_data)
    if(response.status_code==500):
        return True
    elif(response.status_code==404):
        return False
    
    