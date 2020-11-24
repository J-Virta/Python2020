#Search jobs by set attributes(job type, location)

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

jobs = [] # List of available IT-jobs @@@@
location = [] # List of location set for job search

driver.get("@@@@@") # URL 

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
pass

for a in soup.findAll('a',href=True):
availablejobs = a.find ('div', attrs={'class':'Tieto- ja tietoliikennetekniikka'}) # search class for the type of job
searchlocation = a.find ('div', attrs={'class':'Uusimaa'}) # search class for the job location

jobs.append(jobs.text)
location.append(location.text)

df = pd.DataFrame({'List of IT-jobs':jobs, 'SetLocation':location})
df.to_csv('jobs.csv', index=False, encoding='UTF-8')