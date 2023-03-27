from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json

url = 'https://scholar.google.com/'
searchString = input("What do you want to search: ")
print("")


##driver = webdriver.Chrome()
##driver.get(url)
##
##SearchBox = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
##SearchBox.send_keys(searchString)
##
##searchButton = driver.find_element_by_xpath('//*[@id="gs_hdr_tsb"]/span/span[1]')
##searchButton.click()

baseURL = 'https://scholar.google.com/scholar'
parameters = {'hl':'en', 'q': searchString}
response = requests.get(baseURL, params = parameters)
soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all("h3", class_="gs_rt")
i = 1
for result in results:
    linkHeaders = result.find_all("a")
    for link in linkHeaders:
        print(str(i) + ") " + link.text)
        print("")
    i += 1

choice = int(input("Enter your choice: "))
resultChoice = results[choice - 1]

linkHeaders = resultChoice.find_all("a")
for link in linkHeaders:
    print(link.text)
    print("")


