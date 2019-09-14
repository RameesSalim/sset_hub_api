from flask import Flask,request,render_template,redirect,url_for
from flask import session
import requests
import mechanize 
from bs4 import BeautifulSoup 
import csv
import numpy as np
import json


app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key ='a?Aە*?:?S??N'


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']  and request.form['password']:
            url = "https://sset.ecoleaide.com"
            username = request.form['username']
            password = request.form['password']
            session['username'] = username
            new_url = requests.get(url)
            print(new_url.url)
            #Filtering Session ID from the base URL
            session_filter = str(new_url.url)
            session = session_filter.split(';')
            session = ";" + session[1]
            print(session)
            session['sess'] = session
            #Inputs to submit form
            username = "SSET_" + username 
            # Ecoliade Login Action 
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
            sign_in = br.open(new_url.url)  #the login url
            br.select_form(nr = 0) 
            br.set_all_readonly(False)
            br["username"] =username 
            br["password"] =password  
            logged_in = br.submit()  
            logincheck = logged_in.read()  
            # word = "Change Password"
            if b'Change Password' in logincheck:
                session['username'] = request.form['username']
                # session['password'] = password
                return render_template('index.html')
        
            # print(logincheck)
            # return redirect(url_for('home'))
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return 'Home'


if __name__ == '__main__':
   app.run(debug = True)