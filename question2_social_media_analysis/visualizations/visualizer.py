
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations():
    """
    Creates and saves various plots from the cleaned book data.
    """
    # Define the file path for the input file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_processing', 'cleaned_books.csv')

    print(f"Reading cleaned data from {input_file_path}...")

    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    # Set the style for the plots
    sns.set_style("whitegrid")
    
    # --- Plot 1: Price Distribution Histogram ---
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], bins=20, kde=True)
    plt.title('Price Distribution of Books')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    plt.savefig('price_distribution_histogram.png')
    plt.close()
    print("Saved 'price_distribution_histogram.png'")

    # --- Plot 2: Box Plot of Prices by Category ---
    plt.figure(figsize=(15, 8))
    sns.boxplot(x='category', y='price', data=df)
    plt.title('Price Distribution by Category')
    plt.xlabel('Category')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('price_by_category_boxplot.png')
    plt.close()
    print("Saved 'price_by_category_boxplot.png'")

    # --- Plot 3: Category Popularity Bar Chart ---
    plt.figure(figsize=(12, 7))
    category_counts = df['category'].value_counts().nlargest(10)
    sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')
    plt.title('Top 10 Most Popular Book Categories')
    plt.xlabel('Category')
    plt.ylabel('Number of Books')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('category_popularity_barchart.png')
    plt.close()
    print("Saved 'category_popularity_barchart.png'")

if __name__ == "__main__":
    create_visualizations()