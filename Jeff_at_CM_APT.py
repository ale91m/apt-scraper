#########################################################
###### Web Scraping Jefferson @ Carmel Mountain APT######
#########################################################

#import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date
import numpy as np
import pandas as pd

#insert the website you want to scrape. Urlopen isn't working
url = "https://www.liveatjeffersonatcarmelmtn.com/floorplans"
page = urlopen(url)
#I also tried the following, that doesn't work either
from urllib.request import Request
req = Request('https://www.liveatjeffersonatcarmelmtn.com/floorplans')
webpage = urlopen(req).read()
