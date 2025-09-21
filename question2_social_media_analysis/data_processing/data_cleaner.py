# question2_social_media_analysis/data_processing/data_cleaner.py

import pandas as pd
import re
import os

def convert_rating(rating_text):
    """Converts text ratings to numerical values."""
    ratings = {
        'One': 1, 'Two': 2, 'Three': 3,
        'Four': 4, 'Five': 5
    }
    return ratings.get(rating_text, 0) # Returns 0 if not found

def clean_data():
    """
    Reads the scraped book data, cleans it, and saves the cleaned data to a new CSV.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_collection', 'scraped_books.csv')
    output_file_path = os.path.join(current_dir, 'cleaned_books.csv')

    print(f"Reading data from {input_file_path}...")

    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    print("Cleaning and preprocessing data...")

    # Handle duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_count - len(df)
    print(f"Removed {duplicates_removed} duplicate rows.")

    # Clean the price column
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Clean and convert the rating column
    df['rating'] = df['rating'].apply(convert_rating)
    
    # Handle missing data
    missing_data_count = df.isnull().sum().sum()
    if missing_data_count > 0:
        print(f"Handling {missing_data_count} missing values by dropping rows.")
        df.dropna(inplace=True)

    print("Data cleaning complete.")
    
    # Save the cleaned data to a new CSV file
    df.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to {output_file_path}")

if __name__ == "__main__":
    clean_data()