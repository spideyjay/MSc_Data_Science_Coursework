import pandas as pd
import os

def perform_analysis():
    """
    Performs statistical analysis on the cleaned book data.
    """
    # Define the file path for the input file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_processing', 'cleaned_books.csv')

    print(f"Reading cleaned data from {input_file_path}...")

    # Load the cleaned data into a pandas DataFrame
    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    # --- Descriptive Statistics ---
    print("\n--- Descriptive Statistics ---")
    print("Price Summary:")
    print(df['price'].describe())
    print("\nCategory Frequency Distribution:")
    print(df['category'].value_counts())

    # --- Price Analysis by Category ---
    print("\n--- Price Analysis by Category ---")
    category_price_stats = df.groupby('category')['price'].agg(['mean', 'median', 'std']).sort_values(by='mean', ascending=False)
    print(category_price_stats)

    # --- Outlier Detection (using IQR) ---
    print("\n--- Outlier Detection for Prices ---")
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
    print(f"Found {len(outliers)} price outliers.")
    if not outliers.empty:
        print("Outlier details:")
        print(outliers[['title', 'price', 'category']].sort_values(by='price', ascending=False))

    # --- Correlation Analysis ---
    # Note: We don't have a 'rating' or 'availability' column in the scraped data.
    # This section is a placeholder to show the methodology.
    # In a real-world scenario, you would perform correlation on relevant columns.
    # For now, we will simply print a message about this limitation.
    print("\n--- Correlation Analysis ---")
    print("Note: The scraped data from books.toscrape.com does not include a numerical rating. "
          "Therefore, correlation analysis cannot be performed as specified in the coursework. "
          "This section serves as a placeholder for the methodology.")
    
    # --- Category Popularity Analysis ---
    print("\n--- Top 5 Most Popular Categories ---")
    # Assuming popularity is measured by the number of books in the category
    top_categories = df['category'].value_counts().head(5)
    print(top_categories)


if __name__ == "__main__":
    perform_analysis()