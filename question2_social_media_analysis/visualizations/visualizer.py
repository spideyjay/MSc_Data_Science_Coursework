# question2_social_media_analysis/visualizations/visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import os

def create_static_visualizations(df):
    """Create traditional matplotlib/seaborn visualizations"""
    sns.set_style("whitegrid")
    
    # Price Distribution by Source
    plt.figure(figsize=(12, 6))
    if 'source' in df.columns:
        for source in df['source'].unique():
            source_data = df[df['source'] == source]['price']
            plt.hist(source_data, alpha=0.7, label=source, bins=20)
        plt.legend()
    else:
        plt.hist(df['price'], bins=20)
    plt.title('Price Distribution by Data Source')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('price_distribution_by_source.png')
    plt.close()
    
    # Rating vs Price Scatter by Category
    if 'rating' in df.columns and 'category' in df.columns:
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=df, x='rating', y='price', hue='category', alpha=0.7)
        plt.title('Price vs Rating by Category')
        plt.xlabel('Rating')
        plt.ylabel('Price ($)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig('price_vs_rating_by_category.png')
        plt.close()

def create_interactive_visualizations(df):
    """Create interactive Plotly visualizations"""
    
    # Interactive Price Distribution by Source
    if 'source' in df.columns:
        fig = px.histogram(df, x='price', color='source', 
                          title='Interactive Price Distribution by Source',
                          labels={'price': 'Price ($)', 'count': 'Number of Products'},
                          opacity=0.7)
        fig.write_html('interactive_price_distribution.html')
    
    # Interactive Scatter Plot: Price vs Rating
    if 'rating' in df.columns:
        fig = px.scatter(df, x='rating', y='price', color='category',
                        title='Price vs Rating Interactive Scatter Plot',
                        hover_data=['title', 'source'],
                        labels={'rating': 'Rating', 'price': 'Price ($)'})
        fig.write_html('interactive_price_rating_scatter.html')
    
    # Comparative Box Plots by Source and Category
    if 'source' in df.columns and 'category' in df.columns:
        fig = px.box(df, x='source', y='price', color='category',
                    title='Price Distribution by Source and Category')
        fig.write_html('interactive_comparative_boxplot.html')
    
    # Interactive Heatmap of Correlations
    numerical_df = df.select_dtypes(include=['number'])
    if len(numerical_df.columns) > 1:
        corr_matrix = numerical_df.corr()
        fig = px.imshow(corr_matrix, 
                       title='Correlation Matrix Heatmap',
                       color_continuous_scale='RdBu_r',
                       aspect='auto')
        fig.write_html('interactive_correlation_heatmap.html')
    
    # Time Series Analysis (if date available)
    if 'scraped_at' in df.columns:
        df['scraped_date'] = pd.to_datetime(df['scraped_at']).dt.date
        daily_stats = df.groupby('scraped_date').agg({
            'price': 'mean',
            'rating': 'mean' if 'rating' in df.columns else None
        }).reset_index()
        
        fig = px.line(daily_stats, x='scraped_date', y='price',
                     title='Average Price Trend Over Time')
        fig.write_html('price_trend_over_time.html')

def create_comparative_analysis_plots(df):
    """Create plots specifically for comparative analysis between sources"""
    
    if 'source' not in df.columns:
        return
    
    # Comparative pricing analysis
    source_price_stats = df.groupby('source').agg({
        'price': ['mean', 'median', 'std', 'count']
    }).round(2)
    
    # Create comparative bar chart
    fig = px.bar(x=source_price_stats.index, 
                y=source_price_stats[('price', 'mean')],
                title='Average Price Comparison Across Sources',
                labels={'x': 'Data Source', 'y': 'Average Price ($)'})
    fig.write_html('average_price_comparison.html')
    
    # Category distribution across sources
    if 'category' in df.columns:
        category_source_counts = pd.crosstab(df['category'], df['source'], normalize='columns') * 100
        fig = px.imshow(category_source_counts,
                       title='Category Distribution Across Sources (%)',
                       color_continuous_scale='Blues')
        fig.write_html('category_distribution_heatmap.html')

def create_advanced_visualizations(df):
    """Create advanced statistical visualizations"""
    
    # Q-Q plot for normality check (using plotly)
    if len(df) > 0:
        import scipy.stats as stats
        price_data = df['price'].dropna()
        theoretical_quantiles = stats.probplot(price_data, dist="norm")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=theoretical_quantiles[0][0], 
                                y=theoretical_quantiles[0][1],
                                mode='markers',
                                name='Actual vs Theoretical'))
        fig.add_trace(go.Scatter(x=theoretical_quantiles[0][0],
                                y=theoretical_quantiles[1][0] * theoretical_quantiles[0][0] + theoretical_quantiles[1][1],
                                mode='lines',
                                name='Normal Distribution'))
        fig.update_layout(title='Q-Q Plot: Price Distribution Normality Check',
                         xaxis_title='Theoretical Quantiles',
                         yaxis_title='Sample Quantiles')
        fig.write_html('qq_plot_price_normality.html')

def create_visualizations():
    """
    Creates comprehensive static and interactive visualizations
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'data_processing', 'cleaned_products.csv')

    print(f"Reading cleaned data from {input_file_path}...")

    try:
        df = pd.read_csv(input_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return

    print("Creating visualizations...")
    
    # Create static visualizations
    create_static_visualizations(df)
    print("Static visualizations created and saved.")
    
    # Create interactive visualizations
    create_interactive_visualizations(df)
    print("Interactive Plotly visualizations created and saved.")
    
    # Create comparative analysis plots
    create_comparative_analysis_plots(df)
    print("Comparative analysis plots created and saved.")
    
    # Create advanced statistical visualizations
    create_advanced_visualizations(df)
    print("Advanced statistical visualizations created and saved.")
    
    print("All visualizations completed successfully!")

if __name__ == "__main__":
    create_visualizations()