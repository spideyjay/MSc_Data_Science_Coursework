# question2_social_media_analysis/data_processing/data_cleaner.py

import pandas as pd
import re
import os
import numpy as np
from datetime import datetime
from textblob import TextBlob

def clean_text(text):
    """Advanced text cleaning and normalization"""
    if pd.isna(text):
        return ""
    
    text = str(text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s\.\,\!\?]', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Convert to lowercase for consistency
    text = text.lower()
    
    return text

def extract_sentiment(text):
    """Extract sentiment score from text descriptions"""
    if pd.isna(text) or text == "":
        return 0.0
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0.0

def extract_hashtags_mentions(text):
    """Extract hashtags and mentions from text (for social media analysis)"""
    if pd.isna(text):
        return [], []
    
    text = str(text)
    hashtags = re.findall(r'#\w+', text)
    mentions = re.findall(r'@\w+', text)
    
    return hashtags, mentions

def standardize_availability(avail_text):
    """Standardize availability descriptions"""
    if pd.isna(avail_text):
        return "Unknown"
    
    text = str(avail_text).lower()
    if any(word in text for word in ['in stock', 'available', 'instock']):
        return "In Stock"
    elif any(word in text for word in ['out of stock', 'unavailable']):
        return "Out of Stock"
    else:
        return "Unknown"

def convert_rating(rating):
    """Enhanced rating conversion handling multiple formats"""
    if pd.isna(rating):
        return 0
    
    rating = str(rating)
    
    # Handle textual ratings (One, Two, etc.)
    text_ratings = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    if rating.lower() in text_ratings:
        return text_ratings[rating.lower()]
    
    # Handle numeric ratings
    try:
        return float(rating)
    except:
        return 0

def validate_data(df):
    """Comprehensive data validation"""
    validation_issues = []
    
    # Price validation
    invalid_prices = df[df['price'] <= 0]
    if len(invalid_prices) > 0:
        validation_issues.append(f"Found {len(invalid_prices)} records with invalid prices")
    
    # Rating validation
    invalid_ratings = df[(df['rating'] < 0) | (df['rating'] > 5)]
    if len(invalid_ratings) > 0:
        validation_issues.append(f"Found {len(invalid_ratings)} records with invalid ratings")
    
    # Missing critical fields
    missing_titles = df[df['title'].isna() | (df['title'] == '')]
    if len(missing_titles) > 0:
        validation_issues.append(f"Found {len(missing_titles)} records with missing titles")
    
    return validation_issues

def clean_data():
    """
    Enhanced data cleaning pipeline with comprehensive preprocessing
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_collection', 'scraped_products.csv')
    output_file_path = os.path.join(current_dir, 'cleaned_products.csv')

    print(f"Reading data from {input_file_path}...")

    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    print("Starting comprehensive data cleaning...")
    initial_count = len(df)

    # 1. Handle duplicates
    df.drop_duplicates(subset=['title', 'source'], inplace=True)
    print(f"Removed {initial_count - len(df)} duplicate rows.")

    # 2. Text preprocessing
    df['title_clean'] = df['title'].apply(clean_text)
    if 'description' in df.columns:
        df['description_clean'] = df['description'].apply(clean_text)
        df['sentiment_score'] = df['description_clean'].apply(extract_sentiment)
        
        # Extract hashtags and mentions
        df[['hashtags', 'mentions']] = df['description_clean'].apply(
            lambda x: pd.Series(extract_hashtags_mentions(x))
        )

    # 3. Standardize numerical fields
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['rating'] = df['rating'].apply(convert_rating)
    
    # Ensure rating is between 0-5
    df['rating'] = df['rating'].clip(0, 5)

    # 4. Standardize categorical fields
    if 'availability' in df.columns:
        df['availability_standardized'] = df['availability'].apply(standardize_availability)
    
    # 5. Date/time standardization
    if 'scraped_at' in df.columns:
        df['scraped_at'] = pd.to_datetime(df['scraped_at'], errors='coerce')

    # 6. Handle missing data strategically
    missing_before = df.isnull().sum().sum()
    
    # Drop rows missing critical information
    critical_columns = ['title', 'price']
    df = df.dropna(subset=critical_columns)
    
    # For less critical columns, use appropriate imputation
    if 'rating' in df.columns:
        df['rating'].fillna(df['rating'].median(), inplace=True)
    
    missing_after = df.isnull().sum().sum()
    print(f"Reduced missing values from {missing_before} to {missing_after}")

    # 7. Data validation
    validation_issues = validate_data(df)
    if validation_issues:
        print("Validation issues found:")
        for issue in validation_issues:
            print(f"  - {issue}")
    else:
        print("Data validation passed successfully")

    # 8. Create additional features
    df['price_category'] = pd.cut(df['price'], 
                                 bins=[0, 10, 25, 50, 100, float('inf')],
                                 labels=['Budget', 'Affordable', 'Mid-range', 'Premium', 'Luxury'])
    
    df['rating_category'] = pd.cut(df['rating'],
                                  bins=[0, 1, 2, 3, 4, 5],
                                  labels=['Very Poor', 'Poor', 'Average', 'Good', 'Excellent'])

    print(f"Data cleaning complete. Final dataset: {len(df)} records")
    
    # Save cleaned data
    df.to_csv(output_file_path, index=False)
    print(f"Cleaned data saved to {output_file_path}")
    
    return df

if __name__ == "__main__":
    clean_data()