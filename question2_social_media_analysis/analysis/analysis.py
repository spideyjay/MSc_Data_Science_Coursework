# question2_social_media_analysis/analysis/analysis.py

import pandas as pd
import numpy as np
import os
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def perform_comparative_analysis(df):
    """Comparative analysis between different data sources"""
    print("\n=== COMPARATIVE ANALYSIS BETWEEN SOURCES ===")
    
    if 'source' not in df.columns:
        print("No source information available for comparative analysis")
        return
    
    # Price comparison by source
    source_price_stats = df.groupby('source')['price'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)
    print("\nPrice Statistics by Source:")
    print(source_price_stats)
    
    # Rating comparison by source
    if 'rating' in df.columns:
        source_rating_stats = df.groupby('source')['rating'].agg([
            'mean', 'median', 'std', 'count'
        ]).round(2)
        print("\nRating Statistics by Source:")
        print(source_rating_stats)
    
    # Category distribution by source
    if 'category' in df.columns:
        category_cross = pd.crosstab(df['source'], df['category'], normalize='index') * 100
        print("\nCategory Distribution by Source (%):")
        print(category_cross.round(2))

def perform_hypothesis_testing(df):
    """Advanced hypothesis testing"""
    print("\n=== HYPOTHESIS TESTING ===")
    
    # Example: Test if prices differ significantly between sources
    sources = df['source'].unique()
    if len(sources) >= 2:
        source1_data = df[df['source'] == sources[0]]['price'].dropna()
        source2_data = df[df['source'] == sources[1]]['price'].dropna()
        
        if len(source1_data) > 0 and len(source2_data) > 0:
            t_stat, p_value = stats.ttest_ind(source1_data, source2_data, equal_var=False)
            print(f"\nT-test between {sources[0]} and {sources[1]} prices:")
            print(f"T-statistic: {t_stat:.3f}, P-value: {p_value:.3f}")
            
            if p_value < 0.05:
                print("Significant difference found between source prices (p < 0.05)")
            else:
                print("No significant difference between source prices")
    
    # Test correlation between price and rating
    if 'rating' in df.columns:
        corr_coef, p_value = stats.pearsonr(df['price'].dropna(), df['rating'].dropna())
        print(f"\nCorrelation between Price and Rating:")
        print(f"Correlation coefficient: {corr_coef:.3f}, P-value: {p_value:.3f}")

def perform_advanced_statistical_analysis(df):
    """Comprehensive statistical analysis"""
    print("\n=== ADVANCED STATISTICAL ANALYSIS ===")
    
    # Normality tests
    if len(df) > 0:
        price_normality = stats.shapiro(df['price'].dropna())
        print(f"\nNormality test for prices (Shapiro-Wilk):")
        print(f"W-statistic: {price_normality[0]:.3f}, P-value: {price_normality[1]:.3f}")
    
    # Outlier detection using multiple methods
    print("\n=== OUTLIER DETECTION ===")
    
    # IQR method
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    iqr_outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
    print(f"IQR method outliers: {len(iqr_outliers)}")
    
    # Z-score method
    z_scores = np.abs(stats.zscore(df['price'].dropna()))
    z_outliers = df.iloc[np.where(z_scores > 3)[0]]
    print(f"Z-score method outliers (|Z| > 3): {len(z_outliers)}")
    
    if not iqr_outliers.empty:
        print("\nTop 5 price outliers (IQR method):")
        print(iqr_outliers[['title', 'price', 'source', 'category']].sort_values('price', ascending=False).head())

def perform_analysis():
    """
    Performs comprehensive statistical analysis on the cleaned product data.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_processing', 'cleaned_products.csv')

    print(f"Reading cleaned data from {input_file_path}...")

    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return None

    print(f"Dataset shape: {df.shape}")

    # --- Basic Descriptive Statistics ---
    print("\n=== DESCRIPTIVE STATISTICS ===")
    print("Price Summary:")
    print(df['price'].describe())
    
    if 'rating' in df.columns:
        print("\nRating Summary:")
        print(df['rating'].describe())

    # --- Frequency Distributions ---
    if 'category' in df.columns:
        print("\nCategory Frequency Distribution:")
        print(df['category'].value_counts())
    
    if 'availability_standardized' in df.columns:
        print("\nAvailability Frequency Distribution:")
        print(df['availability_standardized'].value_counts())

    # --- Grouped Analysis ---
    if 'category' in df.columns:
        print("\n=== PRICE AND RATING ANALYSIS BY CATEGORY ===")
        category_stats = df.groupby('category').agg({
            'price': ['count', 'mean', 'median', 'std', 'min', 'max'],
            'rating': ['mean', 'median', 'std'] if 'rating' in df.columns else []
        }).round(2)
        print(category_stats)

    # --- Correlation Analysis ---
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    if len(numerical_columns) > 1:
        print("\n=== CORRELATION MATRIX ===")
        correlation_matrix = df[numerical_columns].corr()
        print(correlation_matrix)

    # --- Advanced Analyses ---
    perform_comparative_analysis(df)
    perform_hypothesis_testing(df)
    perform_advanced_statistical_analysis(df)
    
    return df

def perform_predictive_analysis(df):
    """
    Enhanced predictive analysis with multiple models
    """
    if df is None or len(df) == 0:
        print("Cannot perform predictive analysis: DataFrame is empty.")
        return
    
    print("\n=== PREDICTIVE ANALYSIS ===")
    
    # Prepare data for modeling
    model_df = df.dropna(subset=['price', 'rating']) if 'rating' in df.columns else df.dropna(subset=['price'])
    
    if len(model_df) < 10:
        print("Insufficient data for predictive modeling")
        return
    
    # Feature engineering
    features = []
    
    # Categorical features
    if 'category' in model_df.columns:
        encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        category_encoded = encoder.fit_transform(model_df[['category']])
        category_df = pd.DataFrame(category_encoded, columns=encoder.get_feature_names_out(['category']))
        features.append(category_df)
    
    # Numerical features
    numerical_features = ['rating'] if 'rating' in model_df.columns else []
    if numerical_features:
        features.append(model_df[numerical_features])
    
    if not features:
        print("No suitable features for predictive modeling")
        return
    
    X = pd.concat(features, axis=1)
    y = model_df['price']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred = lr_model.predict(X_test)
    
    # Model evaluation
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"Linear Regression Results:")
    print(f"R-squared: {r2:.3f}")
    print(f"Mean Squared Error: {mse:.3f}")
    
    # Feature importance
    if hasattr(lr_model, 'coef_'):
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'coefficient': lr_model.coef_
        }).sort_values('coefficient', key=abs, ascending=False)
        
        print("\nTop 10 Most Important Features:")
        print(feature_importance.head(10))

def create_recommendation_system(df):
    """
    Basic recommendation system based on product similarity
    """
    print("\n=== RECOMMENDATION SYSTEM ===")
    
    if 'category' not in df.columns or 'rating' not in df.columns:
        print("Insufficient data for recommendation system")
        return
    
    # Simple content-based filtering
    def recommend_similar_products(product_title, n_recommendations=5):
        product = df[df['title'] == product_title].iloc[0]
        same_category = df[df['category'] == product['category']]
        similar_products = same_category[same_category['title'] != product_title]
        
        # Sort by rating and price similarity
        similar_products = similar_products.sort_values(
            by=['rating', 'price'], 
            ascending=[False, True]
        )
        
        return similar_products.head(n_recommendations)
    
    # Test the recommendation system
    if len(df) > 0:
        sample_product = df.iloc[0]['title']
        recommendations = recommend_similar_products(sample_product, 3)
        
        print(f"Recommendations similar to '{sample_product}':")
        for idx, row in recommendations.iterrows():
            print(f"  - {row['title']} (Rating: {row['rating']}, Price: ${row['price']:.2f})")

def analyze_availability_pricing_relationship(df):
    """
    Analyze relationship between availability and pricing
    """
    print("\n=== AVAILABILITY vs PRICING ANALYSIS ===")
    
    if 'availability_standardized' not in df.columns:
        print("Availability data not available for analysis")
        return
    
    availability_stats = df.groupby('availability_standardized').agg({
        'price': ['mean', 'median', 'count'],
        'rating': 'mean' if 'rating' in df.columns else []
    }).round(2)
    
    print("Pricing and Rating by Availability Status:")
    print(availability_stats)
    
    # Statistical test for price differences by availability
    availability_groups = [group for name, group in df.groupby('availability_standardized')]
    if len(availability_groups) >= 2:
        f_stat, p_value = stats.f_oneway(*[group['price'].dropna() for group in availability_groups])
        print(f"\nANOVA test for price differences by availability:")
        print(f"F-statistic: {f_stat:.3f}, P-value: {p_value:.3f}")

if __name__ == "__main__":
    cleaned_df = perform_analysis()
    if cleaned_df is not None:
        perform_predictive_analysis(cleaned_df)
        create_recommendation_system(cleaned_df)
        analyze_availability_pricing_relationship(cleaned_df)