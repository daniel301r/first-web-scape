# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:02:15 2018

@author: Me
"""

from random import choice
from csv import DictReader

def read_books(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)
        

def start_game(books):
    book_1 = choice(books)
    book_2 = choice(books)
    while book_1 == book_2:
        book_2 = choice(books)
    print("Which of these two book titles is more highly rated?\nJust type the title number or 3 for a draw")
    print(f"Title 1: {book_1['Title']}\nTitle 2: {book_2['Title']}")
    resp = int(input())
    
    def rating(book):
        if book['Rating'] == "One":
            return 1
        elif book['Rating'] == "Two":
            return 2
        elif book['Rating'] == "Three":
            return 3
        elif book['Rating'] == "Four":
            return 4
        else:
            return 5

    winner = 0
    if rating(book_1) > rating(book_2):
        winner = 1
    elif rating(book_1) < rating(book_2):
        winner = 2
    else:
        winner = 3
          
    if resp == winner:
        print("You guessed correctly!!")
        print(f"The rating for {book_1['Title']} is {book_1['Rating']} and the rating for {book_2['Title']} is {book_2['Rating']}\n")
    else:
        print("You got it wrong!!")
        print(f"The rating for {book_1['Title']} is {book_1['Rating']} and the rating for {book_2['Title']} is {book_2['Rating']}\n")
    
    if winner == 1:
        print(f"Now we know that {book_1['Title']} is more highly ranked than {book_2['Title']}.....\nDo you want to guess which book costs more (y/n)?")
    elif winner == 2:
        print(f"Now we know that {book_2['Title']} is more highly ranked than {book_1['Title']}.....\nDo you want to guess which book costs more (y/n)?")
    else:
        print(f"Now we know that {book_1['Title']} is as highly ranked as {book_2['Title']}.......do you want to guess which book costs more (y/n)?")
        
    def cost_guess(books):
        print(f"So which one is more expensive? Title 1: {book_1['Title']} or Title 2: {book_2['Title']}")
        ans = int(input())
        if book_1["Price"][1:] > book_2["Price"][1:] and ans == 1:
            print(f"You got it right!! Title 1: {book_1['Title']} costs {book_1['Price']} and Title 2: {book_2['Title']} costs {book_2['Price']}")
        elif book_1["price"][1:] < book_2["price"][1:] and ans == 2:
            print(f"You got it right!! Title 1: {book_1['Title']} costs {book_1['Price']} and Title 2: {book_2['Title']} costs {book_2['Price']}")
        else:
            print(f"You got it wrong!! Title 1: {book_1['Title']} costs {book_1['Price']} and Title 2: {book_2['Title']} costs {book_2['Price']}")
        
    again = ""
    while again.lower() not in ("y","yes","n","no"):
        again = input()
    if again in ("y","yes"):
        cost_guess(books)
    else:
        print("Ok see you again soon!!")
        
books = read_books("books.csv")
# print(books)
start_game(books)
