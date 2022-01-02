from logging import debug
from flask.json import jsonify
from query import *
import flask
from flask_restful import Api, Resource, reqparse, abort
import json

app = flask.Flask(__name__)
api = Api(app)

def abort_register(user, password, confirm_password):
    if password != confirm_password:
        abort(404, message='Confirm password does not match')
    if user:
        abort(404, message='Username existed')

def abort_login(user):
    if not user:
        abort(404, message='Username does not exist or password is wrong')

@app.route("/users/login/", methods=["GET"])
def login():
    json_data = json.loads(flask.request.get_json())
    username = json_data["username"]
    user = selectUser(username)
    abort_login(user)
    return {'password': str(user)}

@app.route("/users/register/", methods=["POST"])
def register():
    json_data = json.loads(flask.request.get_json())
    username = json_data["username"]
    password = json_data["password"]
    confirm_password = json_data["confirm_password"]
    publickey = json_data["publickey"]
    user = selectUser(username)
    abort_register(user, password, confirm_password)
    insertUser(username, password, publickey)
    return ''

@app.route("/images/", methods=["POST"])
def getImage():
    # file = flask.request.files['file']
    # print(file)
    # print(flask.request.get_json())
    # json_data = json.loads(flask.request.get_json())
    # username = json_data["username"]
    # print(username)
    # image_name = json_data["image_name"]

    return ''

# api.add_resource(UsersLogin, "/users/login")
# api.add_resource(UsersRegister, "users/register")

if __name__ == "__main__":
    app.run() # debug=True to log all output/debug