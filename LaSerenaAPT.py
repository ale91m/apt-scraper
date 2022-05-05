##############################################
##### Web scraping La Serena Apartments ######
##############################################

#importing
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date
import numpy as np
import pandas as pd

#insert the website you want to scrape
url = "https://www.laserenasd.com/floorplans"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#to print the html you can use:
#print(soup)
#print(soup.get_text())
#print(soup.prettify())

#find type apartment string format
apt_types_matches = len (soup.find_all(class_="card-title h4 font-weight-bold text-capitalize"))
apt = np.empty(apt_types_matches, dtype = object)
apt_types = soup.find_all(class_="card-title h4 font-weight-bold text-capitalize")
i=0
for i in range (0, apt_types_matches):
    apt[i] = apt_types[i].get_text()
#find squared feets for each apt
apt_sqft_matches = len (soup.find_all(class_="d-flex align-items-center"))
sqft = np.empty(apt_sqft_matches, dtype = object)
apt_sqft = soup.find_all(class_="d-flex align-items-center")
k=0
for k in range (0, apt_sqft_matches):
    sqft[k] = apt_sqft[k].get_text()
#find price for each apt
apt_price_matches = len(soup.find_all(class_="font-weight-bold mb-1 text-md"))
price = np.empty(apt_price_matches, dtype = int)
apt_prices = soup.find_all(class_="font-weight-bold mb-1 text-md")
price_index = np.empty(apt_price_matches, dtype = int)
j=0
for j in range (0, apt_price_matches):
    price_index[j] = apt_prices[j].get_text().find('$')
    price[j] = int(apt_prices[j].get_text()[price_index[j] + 1] +
                   apt_prices[j].get_text()[price_index[j] + 3 : price_index[j] + 6])
#save today date
today = date.today()
tdy = today.strftime("%b-%d-%Y")

#data definition
data = {'date' : [tdy, tdy],
        'price $' : [price[0], price[1]],
        'sqft' : [sqft[2], sqft[5]]}
table = pd.DataFrame(data = data, index = [apt[0], apt[1]])
table.to_csv('prova.csv', mode='a', index=True, header=False)

