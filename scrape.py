import requests
import mechanize 
from bs4 import BeautifulSoup 
import csv
import numpy as np
import json
import http.cookiejar
import datetime

#Base URL 
url = "https://sset.ecoleaide.com"
new_url = requests.get(url)
# print(new_url.url)

#Filtering Session ID from the base URL

session_filter = str(new_url.url)
session = session_filter.split(';')
session = ";" + session[1]
# print(session)



#Inputs to submit form


# username = input("Enter username :")
# password = input("Enter Password :")

username = "SEE/7448/16"
password = "7448"


username = "SSET_" + username 

# Ecoliade Login Action 

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

#Cookie Setup
# Cookie Jar
try:
	cj = mechanize.CookieJar()
	br.set_cookiejar(cj)
	sign_in = br.open(new_url.url)  #the login url
	br.select_form(nr = 0) 
	br.set_all_readonly(False)
	br["username"] =username 
	br["password"] =password  
	logged_in = br.submit()  
	logincheck = logged_in.read()  
except Exception as e:
	print(e)
#Scrapping Needed Data
new_url = br.geturl()

def selectDate(date):
	new_url = br.open("https://sset.ecoleaide.com/search/subjAttendReport.htm" )
	br.select_form(nr = 0) 
	br.set_all_readonly(False)
	x = datetime.datetime.now()
	if(x.month >=8):
		a = "1/8/"
		date = a+str(x.year)
	else:
		a="1/1/"
		date = a+str(x.year)
	br["fromDate"] =date
	read = br.submit()  
	details = read.read()
	return details


def Attendance():
	new_url = br.open("https://sset.ecoleaide.com/search/subjAttendReport.htm")
	br.select_form(nr = 0) 
	br.set_all_readonly(False)
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
		# print(details)
	except Exception as e:
		print(e)
	soup = BeautifulSoup(details, 'html5lib') 
	# print(soup.prettify()) 
	#Getting Attributes
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

if __name__ == "__main__":
    print(Attendance())
