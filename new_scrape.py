from bs4 import BeautifulSoup
import requests


url = "https://sset.ecoleaide.com"

username = "SEE/6993/13"
password = "69936993"
username = "SSET_" + username 

r = requests.Session()

data = {'username': username, 'password': password}

r = requests.post(url, data = data)

content = r.text

print(content)