from flask import Flask,request,render_template,redirect,url_for
from flask import session
import datetime
import os
import requests
import jsonify
from scrape import Attendance


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key =os.urandom(24)

@app.route('/')
def index():
    # return jsonify(Attendance())
    print("helo")

if __name__ == '__main__':
   app.run(debug = True)