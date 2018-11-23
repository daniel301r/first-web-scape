# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:14:57 2018

@author: Me
"""

import requests

from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all(class_='product_pod')

with open('books.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Price', 'Title']
    csv_writer.writerow(headers)

    for book in books:
        
        string = book.find(class_='price_color').get_text()
        price = string[1:]
        
        title = book.find('h3').contents[0]['title']
        csv_writer.writerow([price, title])


'''
- how I did it before with 2 for loops instead of one

books = soup.select('.product_pod h3 a')

prices = soup.findAll(class_='price_color')

for book in books:
    title = book['title']

for price in prices:
    amount = str(price.get_text())
    finalPrice = amount[1:]

'''