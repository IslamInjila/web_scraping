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
# print(soup.prettify(), 'SOUP')
# print(soup.body)


rows = soup.body.find_all("div", class_="WsMG1c nnK0zc")
# print(rows, 'rows')
# f = csv.writer(open('googleApp_data.csv', 'w'))
# f.writerow(['APP_LIST', 'RATINGS'])
datalist = []
# with open("googleApp_data.csv", "w") as csv_file:
#     writer = csv.writer(csv_file)

for row in rows:
    data = row.get_text()  # Print all occurrences
    # writer.writerow([data])
    datalisting = {
        'APP': data
    }
    datalist.append(datalisting)
df = pd.DataFrame(datalist)
# print(df.head(10), 'df')   


secondlist= []
# csv_file.close()
ratings = driver.find_elements_by_xpath('//div[@role="img"]')
# f = csv.writer(open('googleApp_data.csv', 'a+'))
# with open("googleApp_data.csv", "a") as csv_file:
#     writer = csv.writer(csv_file)
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
      # print(ratings_value, 'ratings_value')
      # writer.writerow([ratings_value])
      # f.writerow([ratings_value])
# csv_file.close()



# find_href = browser.find_elements_by_xpath('//your_xpath')
# for my_href in find_href:
#     print(my_href.get_attribute("href"))


# column = soup.body.find_all("div", class_="pf5lIe")

# for columns in column:

#     columnsdata = columns.get_text()  
#     print(columnsdata, 'columnsdata')












# # ratings = soup.body.find_all(aria-label')
# ratings = soup.body.get_attribute('aria-label')
# print(ratings, 'rate')

# ratings = soup.body.find_all(rows="img")
# for i in rows:
#     # print(i)
#     rating = soup.body.find('div', class_="vQHuPe bUWb7c")
#     print(r, 'rating')

# product = soup.find_all('div',{'class','product-item'})
# # print(product)

# for i in product:
#     # print(i)
#     rating = i.find('span', class_="rating-content")
#     print(rating)














