# from flask.json import jsonify
import requests
import json

BASE="http://127.0.0.1:5000/"
json_data = json.dumps({'username':'suir2', 'password': 'a', 'confirm_password': 'a', 'publickey': '638'})

response = requests.post(BASE + "users/login/", json=json_data)
print(response)