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

@app.route('/v1/profile/attendance', methods=['GET','POST'])
def attendance():
    if (request.method == 'GET'):
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    if ( request.method == 'POST'):
        username=None
        password=None
        if request.is_json:
            data = request.get_json(force=True)
            if 'username' in data:
                username = data['username']
            if 'password' in data:
                password = data['password']
        # data = Attendance(username,password)
        # print(data)
        # return json.dumps(data)x
        return "Success"
if __name__ == '__main__':
   app.run(debug = True)