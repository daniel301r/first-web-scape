# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:14:57 2018

@author: Me
"""

import requests

from bs4 import BeautifulSoup
from time import sleep
from random import choice

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

def start_game(quotes):
    quote_1 = choice(quotes)
    quote_2 = choice(quotes)
    while quote_1 == quote_2:
        quote_2 = choice(quotes)
    print("Which of these two book titles is more highly rated?\nJust type the title number or 3 for a draw")
    print(f"Title 1: {quote_1['title']}\nTitle 2: {quote_2['title']}")
    resp = int(input())
    
    def rating(quote):
        if quote['rating'] == "One":
            return 1
        elif quote['rating'] == "Two":
            return 2
        elif quote['rating'] == "Three":
            return 3
        elif quote['rating'] == "Four":
            return 4
        else:
            return 5

    winner = 0
    if rating(quote_1) > rating(quote_2):
        winner = 1
    elif rating(quote_1) < rating(quote_2):
        winner = 2
    else:
        winner = 3
        
    print(winner)     

        
    if resp == winner:
        print("You guessed correctly!!")
        print(f"The rating for {quote_1['title']} is {quote_1['rating']} and the rating for {quote_2['title']} is {quote_2['rating']}\n")
    else:
        print("You got it wrong!!")
        print(f"The rating for {quote_1['title']} is {quote_1['rating']} and the rating for {quote_2['title']} is {quote_2['rating']}\n")
    
    if winner == 1:
        print(f"Now we know that {quote_1['title']} is more highly ranked than {quote_2['title']}.....\nDo you want to guess which book costs more?")
    elif winner == 2:
        print(f"Now we know that {quote_2['title']} is more highly ranked than {quote_1['title']}.....\nDo you want to guess which book costs more?")
    else:
        print(f"Now we know that {quote_1['title']} is as highly ranked as {quote_2['title']}.......do you want to guess which book costs more (y/n)?")
        
    def cost_guess():
        print("This is going to be the new feature - wait a couple of days!!")
    
    again = ""
    while again.lower() not in ("y","yes","n","no"):
        again = input()
    if again in ("y","yes"):
        cost_guess()
    else:
        print("Ok see you again soon!!")
        
    
    

        
