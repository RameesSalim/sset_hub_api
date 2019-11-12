import requests
import mechanize 
from bs4 import BeautifulSoup 
import csv
import numpy as np
import json
import http.cookiejar
import datetime
import os




def Attendance(username,password):
	print("data is ",username,password)

		#Base URL 
	url = "https://sset.ecoleaide.com"
	new_url = requests.get(url)
	# print(new_url.url)
	#Filtering Session ID from the base URL
	session_filter = str(new_url.url)
	session = session_filter.split(';')
	session = ";" + session[1]
	# username = "SEE/7448/16"
	# password = "7448"
	usernamee = "SSET_" + username
	# Ecoliade Login Action 
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
	#COokie Setting

	cookiejar =mechanize.LWPCookieJar()
	br.set_cookiejar(cookiejar)
	# cj = mechanize.CookieJar()
	# br.set_cookiejar(cj)
	try:
		sign_in = br.open(new_url.url)  #the login url
		br.select_form(nr = 0) 
		br.set_all_readonly(False)
		br["username"] =usernamee
		br["password"] =password  
		logged_in = br.submit()  
		logincheck = logged_in.read() 
		soup = BeautifulSoup(logincheck, 'html5lib') 
		# os.remove('login.html')
		# f=open('login.html','w+')
		# f.write(soup.prettify())
		# f.close()
	except Exception as e:
		print(e)
	val = soup.find(text=username)
	print(username)
	print(val)
	#Scrapping Needed Data
	new_url = br.geturl()
	new_url = br.open("https://sset.ecoleaide.com/search/subjAttendReport.htm" + session)
	soup = BeautifulSoup(new_url,'html5lib')
	# os.remove('attendance.html')
	# f = open('attendance.html','w+')
	# f.write(soup.prettify())
	# f.close()
	br.select_form(nr = 0) 
	br.set_all_readonly(False)

	# Date setting
	x = datetime.datetime.now()
	if(x.month >=8):
		a = "1/8/"
		date = a+str(x.year)
	else:
		a="1/1/"
		date = a+str(x.year)
	try:
		br["fromDate"] =date
		read = br.submit()  
		details = read.read()
		soup = BeautifulSoup(details, 'html5lib') 
		data=[]
		table = soup.find('table', attrs = {'class':'subj-attendance-table'})
		table_body = table.find('tbody')
		rows = table_body.find_all('tr')
		datas = np.array([], dtype=float, ndmin=2)
		i = 0
		for row in rows:
			cols = row.find_all('td')
			cols = [ele.text.strip() for ele in cols]
			data.append([ele for ele in cols if ele])
			data[i] = cols
			i= i+1
		return data
	except Exception as e:
		return "Failed"
		print(e)

