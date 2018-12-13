# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:14:57 2018

@author: Me
"""

import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = "http://books.toscrape.com/catalogue/category/books_1/"

def scrape_quotes():
    url = "page-1.html"
    all_quotes = []
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text, 'html.parser')
        
        
        books = soup.find_all(class_="product_pod")
        
        for book in books:
            all_quotes.append({
                "title": book.find("h3").find("a")["title"],
                "rating": (str(book.find_all(class_="star-rating")).split())[2][:-2],
                "price": book.find(class_="price_color").get_text()[1:]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    return all_quotes

def write_quotes(quotes):
    with open("books.csv", "w") as file:
        headers = ("Title", "Rating", "Price")
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow({
                    "Title": quote["title"],
                    "Rating": quote["rating"],
                    "Price": quote["price"]
            })
        
quotes = scrape_quotes()
write_quotes(quotes)
    
    

        
