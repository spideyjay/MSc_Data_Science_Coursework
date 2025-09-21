
import pandas as pd
import re
import os

def clean_data():
    """
    Reads the scraped book data, cleans it, and saves the cleaned data to a new CSV.
    """
    # Define the file paths for input and output
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_collection', 'scraped_books.csv')
    output_file_path = os.path.join(current_dir, 'cleaned_books.csv')

    print(f"Reading data from {input_file_path}...")

    # Load the data into a pandas DataFrame
    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    # Data Cleaning and Preprocessing
    print("Cleaning and preprocessing data...")

    # Handle duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_count - len(df)
    print(f"Removed {duplicates_removed} duplicate rows.")

    # Convert price column to a numeric format
    # The scraping script already handled this, but this is a good practice for real-world data
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Handle missing data
    missing_data_count = df.isnull().sum().sum()
    if missing_data_count > 0:
        print(f"Handling {missing_data_count} missing values by dropping rows.")
        df.dropna(inplace=True)

    # Clean up the title column (remove special characters, extra spaces)
    df['title'] = df['title'].str.strip()
    # Optional: You can add more complex text preprocessing here if needed for analysis.

    print("Data cleaning complete.")
    
    # Save the cleaned data to a new CSV file
    df.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to {output_file_path}")

if __name__ == "__main__":
    clean_data()