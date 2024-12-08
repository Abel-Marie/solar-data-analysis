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