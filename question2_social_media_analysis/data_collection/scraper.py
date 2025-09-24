# question2_social_media_analysis/data_collection/scraper.py

import requests
from bs4 import BeautifulSoup
import csv
import time
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd

def scrape_books_toscrape():
    """Scrapes book data from http://books.toscrape.com/"""
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []
    page_num = 1

    while True:
        url = base_url.format(page_num)
        print(f"Scraping books.toscrape.com page {page_num}...")

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

            rating_text = book.find('p', class_='star-rating')['class'][1]
            
            book_url = 'http://books.toscrape.com/catalogue/' + book.h3.a['href']
            book_response = requests.get(book_url)
            book_soup = BeautifulSoup(book_response.content, 'html.parser')

            category = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
            availability = book_soup.find('p', class_='instock').text.strip()

            all_books.append({
                'source': 'books_toscrape',
                'title': title,
                'price': price_cleaned,
                'category': category,
                'rating': rating_text,
                'availability': availability,
                'scraped_at': datetime.now().isoformat()
            })
        
        time.sleep(1)
        page_num += 1

    return all_books

def scrape_demo_ecommerce():
    """Scrapes product data from a demo e-commerce site"""
    base_url = "https://webscraper.io/test-sites/e-commerce/allinone/products/{}"
    products = []
    
    for page in range(1, 4):  # Limited to 3 pages for demo
        url = base_url.format(page)
        print(f"Scraping demo e-commerce page {page}...")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Error scraping demo site: {e}")
            continue
            
        soup = BeautifulSoup(response.content, 'html.parser')
        product_cards = soup.find_all('div', class_='card-body')
        
        for card in product_cards:
            try:
                title = card.find('a', class_='title')['title']
                price_text = card.find('h4', class_='price').text
                price = float(price_text.replace('$', '').replace(',', ''))
                
                description = card.find('p', class_='description').text
                rating_element = card.find('div', class_='ratings')
                rating = len(rating_element.find_all('span', class_='glyphicon-star')) if rating_element else 0
                
                products.append({
                    'source': 'demo_ecommerce',
                    'title': title,
                    'price': price,
                    'category': 'Electronics',  # Default category for demo site
                    'rating': rating,
                    'availability': 'In stock',  # Default for demo
                    'description': description,
                    'scraped_at': datetime.now().isoformat()
                })
            except Exception as e:
                print(f"Error parsing product: {e}")
                continue
                
        time.sleep(1)
        
    return products

def parse_rss_feed(rss_url=None):
    """Parses RSS feed for additional product data"""
    if rss_url is None:
        # Choose from these demo RSS feeds:
        rss_options = [
            "https://www.bestbuy.com/site/rss/deals.xml",
            "https://www.walmart.com/feeds/ip/4",
            "https://www.newegg.com/Product/RSS.aspx?Submit=RSSDailyDeals&Depa=1",
            "https://www.rssboard.org/files/sample-rss-2.xml"  # Fallback test feed
        ]
        rss_url = rss_options[0]  # Use first option by default
    
    products = []
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(rss_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        
        for item in root.findall('.//item'):
            try:
                title = item.find('title').text if item.find('title') is not None else "No Title"
                description = item.find('description').text if item.find('description') is not None else "No Description"
                
                # Try to extract price if available
                price = 0.0
                price_elem = item.find('.//{http://base.google.com/ns/1.0}price')
                if price_elem is not None:
                    try:
                        price_text = price_elem.text.replace('$', '').replace(',', '')
                        price = float(price_text)
                    except:
                        pass
                
                # Try to get category
                category_elem = item.find('category')
                category = category_elem.text if category_elem is not None else 'RSS_Products'
                
                products.append({
                    'source': 'rss_feed',
                    'title': title[:200],  # Limit title length
                    'price': price,
                    'category': category,
                    'rating': 0,
                    'availability': 'Available',
                    'description': description[:500] if description else "No description",  # Limit length
                    'scraped_at': datetime.now().isoformat()
                })
            except Exception as e:
                print(f"Error parsing RSS item: {e}")
                continue
                
    except Exception as e:
        print(f"Error fetching RSS feed {rss_url}: {e}")
        
    return products

def scrape_all_sources():
    """Main function to scrape data from all sources"""
    all_data = []
    
    # Scrape from multiple sources
    all_data.extend(scrape_books_toscrape())
    all_data.extend(scrape_demo_ecommerce())
    all_data.extend(parse_rss_feed())
    
    # Save to CSV
    csv_file = 'scraped_products.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        if all_data:
            fieldnames = all_data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
    
    print(f"Scraping complete! {len(all_data)} products saved to {csv_file}")
    return all_data

if __name__ == "__main__":
    scrape_all_sources()