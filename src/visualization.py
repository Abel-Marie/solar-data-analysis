import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def plot_histogram(df, column, bins=20):
    """
    Plot a histogram for a specified column in the DataFrame.
    :param df: The DataFrame containing the data.
    :param column: The column name to plot.
    :param bins: Number of bins in the histogram.
    """
    
    if column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], bins=bins, kde=True, color='skyblue')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
    else:
        print(f"Column {column} not found in the dataframe")
def plot_scatter(df, x_column, y_column):
    """
    Plot a scatter plot for two specified columns in the DataFrame.
    :param df: The DataFrame containing the data.
    :param x_column: The column name for the x-axis.
    :param y_column: The column name for the y-axis.
    """
    if x_column in df.columns and y_column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df[x_column], y=df[y_column], color='orange')
        plt.title(f"Scatter Plot of {x_column} vs {y_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()
    else:
        print(f"Columns {x_column} and/or {y_column} not found in the DataFrame.")
       
def plot_correlation_heatmap(df):
    """
    Plot a heatmap of the correlation matrix of the DataFrame.
    :param df: The DataFrame containing the data.
    """
    corr = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidth=0.5)
    plt.title("Correlation Heatmap")
    plt.show()
    
def plot_pairplot(df, columns): 
    """

    Plot a pairplot for selected columns in the DataFrame.
    :param df: The DataFrame containing the data.
    :param columns: List of column names to include in the pairplot.
    """
    
    df_subset = df[columns]
    sns.pairplot(df_subset)
    plt.subtitle("Pairplot", y=1.02)
    plt.show()
    
def plot_time_series(df, column, time_column):
    """
    Plot a time series graph for the specified column against a time column.
    :param df: The DataFrame containing the data.
    :param column: The column name to plot.
    :param time_column: The time column name.
    """
    if column in df.columns and time_column in df.columns:
        plt.figure(figsize=(12, 6))
        plt.plot(df[time_column], df[column], marker='o', linestyle='-', color='purple')
        plt.title(f"Time Series of {column} vs {time_column}")
        plt.xlabel(time_column)
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.show()
    else:
        print(f"Columns {column} or {time_column} not found in the DataFrame.")
        
        
# Functions to plot time series by month (GHI, DNI, DHI, Tamb)
def plot_time_series_monthly(df, column, time_column):
    
    if column in df.columns and time_column in df.columns:
        df['month'] = df[time_column].dt.month
        monthly_data = df.groupby('month')[column].mean()  
        plt.figure(figsize=(10, 6))
        monthly_data.plot(kind='bar', color='orange')
        plt.title(f'Monthly Average of {column}')
        plt.xlabel('Month')
        plt.ylabel(column)
        plt.xticks(rotation=0)
        plt.show()
    else:
        print(f"Columns {column} or {time_column} not found in the DataFrame.")

# function to plot time series by hour (GHI, DNI, DHI, Tamb)
def plot_time_series_hourly(df, column, time_column):
    
    if column in df.columns and time_column in df.columns:
        df['hour'] = df[time_column].dt.hour
        hourly_data = df.groupby('hour')[column].mean()  
        plt.figure(figsize=(10, 6))
        hourly_data.plot(kind='line', color='blue', marker='o')
        plt.title(f'Hourly Average of {column}')
        plt.xlabel('Hour of the Day')
        plt.ylabel(column)
        plt.xticks(rotation=0)
        plt.show()
    else:
        print(f"Columns {column} or {time_column} not found in the DataFrame.")