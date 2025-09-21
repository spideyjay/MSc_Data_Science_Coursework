# question2_social_media_analysis/data_collection/scraper.py

import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_books():
    """
    Scrapes book data from http://books.toscrape.com/
    and saves it to a CSV file.
    """
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []
    page_num = 1
    
    while True:
        url = base_url.format(page_num)
        print(f"Scraping page {page_num}...")
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
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
            # Clean the price string to remove the currency symbol and convert to float
            price_cleaned = float(price[1:])
            
            # Navigate to the book's detail page to get the category
            book_url = 'http://books.toscrape.com/catalogue/' + book.h3.a['href']
            book_response = requests.get(book_url)
            book_soup = BeautifulSoup(book_response.content, 'html.parser')
            category = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()

            all_books.append({
                'title': title,
                'price': price_cleaned,
                'category': category
            })
        
        # Be a good web citizen by adding a delay between requests
        time.sleep(1)
        page_num += 1

    # Save the data to a CSV file
    csv_file = 'scraped_books.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['title', 'price', 'category']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_books)

    print(f"Scraping complete! {len(all_books)} books saved to {csv_file}")


if __name__ == "__main__":
    scrape_books()