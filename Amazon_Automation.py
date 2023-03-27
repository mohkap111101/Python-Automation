#Script to obtain prices of the different product listings for a given search item in on amazon.

from bs4 import BeautifulSoup
from selenium import webdriver
import requests


search = input("Enter what you want to search: ")
searchStringList = search.split(" ")

url = "https://www.amazon.co.uk/s?k="
for i in range(len(searchStringList)):
    url += searchStringList[i]
    if(i != len(searchStringList)-1):
        url += "+"
#url = "http://airfoiltools.com/search/airfoils"
response = requests.get(url)
print(url)
soup = BeautifulSoup(response.text, "lxml")
print(soup)
ProductNames = soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")
print(ProductNames)
ProductCosts = soup.find_all("span", class_="a-price-whole")
for i in range(len(ProductNames)):
    print(ProductNames[i].text)
    print(ProductCosts[i].text)
    print("")
    
