import urllib
from urllib.request import urlopen as uReq  # Web client
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import pandas as pd
import xlwt

import time
page_url = "https://play.google.com/store/apps?utm_source=emea_Med&utm_medium=hasem&utm_content=Oct1515&utm_campaign=Evergreen&pcampaignid=MKT-EDR-emea-ae-all-Med-hasem-ap-Evergreen-Dec0215-1-BKWS%7cONSEM_kwid_43700009229880556&gclid=Cj0KCQjw1a6EBhC0ARIsAOiTkrEFowDhhKedUUkcikW72SoLpsSbfGuRDF2wB_EP-brYSfwGBBTqKFYaAtYvEALw_wcB&gclsrc=aw.ds";


driver=webdriver.Chrome() #Path to Chrome Driver

 

driver.get(page_url)

# opens the connection and downloads html page from url
uClient = uReq(page_url)
print(uClient, 'RES');

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_html = uClient.read();
uClient.close()

#for parsing data we are using beautiful soup
soup = BeautifulSoup(page_html, 'html.parser')


rows = soup.body.find_all("div", class_="WsMG1c nnK0zc")

datalist = []


for row in rows:
    data = row.get_text()  # Print all occurrences
    # writer.writerow([data])
    datalisting = {
        'APP': data
    }
    datalist.append(datalisting)
df = pd.DataFrame(datalist)
  


secondlist= []

ratings = driver.find_elements_by_xpath('//div[@role="img"]')

for rating in ratings:
    ratings_value = rating.get_attribute("aria-label")
   
    datalisting2 = {
        'RATINGS' : ratings_value
      }
    secondlist.append(datalisting2)
#     print(datalisting2, 'datalisting2')
ds =pd.DataFrame(secondlist)
# print(ds.head(10), 'Ds')
data_frame = pd.DataFrame(df)
result = pd.concat([df, ds], axis=1, join='inner')
# data_frame['ds'] = pd.Series(, index=data_frame.index) 
# print(result.head(40), 'data_frame')
result.to_excel('googleapp.xls', index= False)
  

























