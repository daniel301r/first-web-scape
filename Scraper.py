import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = "http://books.toscrape.com/catalogue/category/books_1/"

def scrape_books():
    url = "page-1.html"
    all_books = []
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text, 'html.parser')
        
        
        books = soup.find_all(class_="product_pod")
        
        for book in books:
            all_books.append({
                "title": book.find("h3").find("a")["title"],
                "rating": (str(book.find_all(class_="star-rating")).split())[2][:-2],
                "price": book.find(class_="price_color").get_text()[1:]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    return all_books

def write_books(books):
    with open("books.csv", "w") as file:
        headers = ("Title", "Rating", "Price")
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for book in books:
            csv_writer.writerow({
                    "Title": book["title"],
                    "Rating": book["rating"],
                    "Price": book["price"]
            })
        
books = scrape_books()
write_books(books)
    
    

        
