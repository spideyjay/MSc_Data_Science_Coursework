# question2_social_media_analysis/analysis/analysis.py

import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def perform_analysis():
    """
    Performs statistical analysis on the cleaned book data.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_processing', 'cleaned_books.csv')

    print(f"Reading cleaned data from {input_file_path}...")

    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return None

    # --- Descriptive Statistics ---
    print("\n--- Descriptive Statistics ---")
    print("Price Summary:")
    print(df['price'].describe())
    print("\nRating Summary:")
    print(df['rating'].describe())
    print("\nCategory Frequency Distribution:")
    print(df['category'].value_counts())
    print("\nAvailability Frequency Distribution:")
    print(df['availability'].value_counts())

    # --- Price Analysis by Category and Rating ---
    print("\n--- Price and Rating Analysis by Category ---")
    category_stats = df.groupby('category').agg(
        avg_price=('price', 'mean'),
        avg_rating=('rating', 'mean')
    ).sort_values(by='avg_price', ascending=False)
    print(category_stats)

    # --- Correlation Analysis ---
    print("\n--- Correlation between Price and Rating ---")
    correlation = df[['price', 'rating']].corr()
    print(correlation)
    
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
        print(outliers[['title', 'price', 'category']].sort_values(by='price', ascending=False).head(5))
        
    # Return the DataFrame at the end of the function
    return df

def perform_predictive_analysis(df):
    """
    Uses a simple linear regression model to predict price based on category and rating.
    """
    if df is None:
        print("Cannot perform predictive analysis: DataFrame is empty.")
        return
        
    print("\n--- Predictive Analysis ---")
    
    # Use one-hot encoding for the categorical 'category' feature
    encoder = OneHotEncoder(handle_unknown='ignore')
    category_encoded = encoder.fit_transform(df[['category']]).toarray()
    
    # Create a DataFrame from the encoded categories
    category_df = pd.DataFrame(category_encoded, columns=encoder.get_feature_names_out(['category']))
    
    # Prepare the feature matrix (X) and target vector (y)
    X = pd.concat([category_df, df[['rating']]], axis=1)
    y = df['price']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate the model
    score = model.score(X_test, y_test)
    print(f"Model R-squared score: {score:.2f}")

    # Display coefficients to show the impact on price
    print("\nModel Coefficients (Impact on Price):")
    coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
    print(coefficients.sort_values(by='Coefficient', ascending=False).head(10))

if __name__ == "__main__":
    cleaned_df = perform_analysis()
    if cleaned_df is not None:
        perform_predictive_analysis(cleaned_df)