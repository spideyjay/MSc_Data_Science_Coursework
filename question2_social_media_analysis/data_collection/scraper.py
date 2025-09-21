# question2_social_media_analysis/data_collection/scraper.py

import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_books():
    """
    Scrapes book data from http://books.toscrape.com/
    including title, price, category, rating, and availability.
    """
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []
    page_num = 1

    while True:
        url = base_url.format(page_num)
        print(f"Scraping page {page_num}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print("End of pages reached.")
                break
            else:
                print(f"HTTP error occurred: {e}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        if not books:
            print("No more books found. Stopping.")
            break

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            price_cleaned = float(price[1:])

            # Extract the rating from the class attribute
            rating_text = book.find('p', class_='star-rating')['class'][1]
            
            # Navigate to the book's detail page to get category and availability
            book_url = 'http://books.toscrape.com/catalogue/' + book.h3.a['href']
            book_response = requests.get(book_url)
            book_soup = BeautifulSoup(book_response.content, 'html.parser')

            category = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
            availability = book_soup.find('p', class_='instock').text.strip()

            all_books.append({
                'title': title,
                'price': price_cleaned,
                'category': category,
                'rating': rating_text,
                'availability': availability
            })
        
        time.sleep(1)
        page_num += 1

    # Save the data to a CSV file
    csv_file = 'scraped_books.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['title', 'price', 'category', 'rating', 'availability']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_books)

    print(f"Scraping complete! {len(all_books)} books saved to {csv_file}")


if __name__ == "__main__":
    scrape_books()