from flask import Flask,request,render_template,redirect,url_for
from flask import session
import datetime
import os
import requests
import jsonify,json
from scrape import Attendance


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key =os.urandom(24)

@app.route('/')
def index():
    # return jsonify(Attendance())
    print("helo")
    return "Hello World"

@app.route('/v1/profile/attendance', methods=['POST'])
def attendance():
    username=None
    password=None
    if request.is_json:
        data = request.get_json(force=True)
        if 'username' in data:
            username = data['username']
        if 'password' in data:
            password = data['password']
    data = Attendance(username,password)
    print(data)
    return json.dumps(data)
if __name__ == '__main__':
   app.run(debug = True)