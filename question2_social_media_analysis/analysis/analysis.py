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

    

## adding predictive analysis section


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def perform_predictive_analysis(df):
    """
    Uses a simple linear regression model to predict price based on category.
    """
    print("\n--- Predictive Analysis ---")
    
    # Use one-hot encoding for the categorical 'category' feature
    encoder = OneHotEncoder(handle_unknown='ignore')
    category_encoded = encoder.fit_transform(df[['category']]).toarray()
    
    # Create a DataFrame from the encoded categories
    category_df = pd.DataFrame(category_encoded, columns=encoder.get_feature_names_out(['category']))
    
    # Prepare the feature matrix (X) and target vector (y)
    X = category_df
    y = df['price']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate the model
    score = model.score(X_test, y_test)
    print(f"Model R-squared score: {score:.2f}")

    # Display coefficients to show the price pattern for each category
    print("\nModel Coefficients (Impact on Price):")
    coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
    print(coefficients.sort_values(by='Coefficient', ascending=False).head(10))

# Modify the main script to call this new function
if __name__ == "__main__":
    df = perform_analysis()
    if df is not None:
        perform_predictive_analysis(df)