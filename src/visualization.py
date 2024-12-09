

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



def plot_histogram(df, column, bins=20):
   
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
    
    corr = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidth=0.5)
    plt.title("Correlation Heatmap")
    plt.show()
    
def plot_pairplot(df, columns): 
    
    df_subset = df[columns]
    sns.pairplot(df_subset)
    plt.suptitle("Pairplot", y=1.02)
    plt.show()

# Time Series Plotting for GHI, DNI, DHI, Tamb
def plot_time_series(df, columns, time_column='Timestamp'):
   
    df[time_column] = pd.to_datetime(df[time_column])
    plt.figure(figsize=(12, 8))
    
    for column in columns:
        if column in df.columns:
            plt.plot(df[time_column], df[column], label=column)
    
    plt.title("Time Series of GHI, DNI, DHI, and Tamb")
    plt.xlabel('Timestamp')
    plt.ylabel('Values')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Impact of Cleaning on ModA and ModB Sensor Readings
def plot_cleaning_impact(df, time_column='Timestamp'):
   
    df[time_column] = pd.to_datetime(df[time_column])
    
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(df[time_column], df['ModA'], label='ModA', color='blue')
    plt.scatter(df[df['Cleaning'] == 1][time_column], df[df['Cleaning'] == 1]['ModA'], color='red', label='Cleaning Event', marker='x')
    plt.title('Impact of Cleaning on ModA')
    plt.xlabel('Timestamp')
    plt.ylabel('ModA Sensor Reading')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(df[time_column], df['ModB'], label='ModB', color='orange')
    plt.scatter(df[df['Cleaning'] == 1][time_column], df[df['Cleaning'] == 1]['ModB'], color='red', label='Cleaning Event', marker='x')
    plt.title('Impact of Cleaning on ModB')
    plt.xlabel('Timestamp')
    plt.ylabel('ModB Sensor Reading')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Wind Analysis (Wind Rose)
def plot_wind_rose(df, wind_direction_column='WD', wind_speed_column='WS'):
   
    import matplotlib.colors as mcolors
    import numpy as np
    
    wind_dir = df[wind_direction_column]
    wind_speed = df[wind_speed_column]
    
    # Remove rows with NaN wind speed or direction
    wind_dir = wind_dir.dropna()
    wind_speed = wind_speed.dropna()
    
    # Create wind rose using a polar plot
    angles = np.deg2rad(wind_dir)  
    plt.figure(figsize=(8, 8))
    plt.subplot(projection='polar')
    

    plt.hist(angles, bins=24, weights=wind_speed, color='lightblue', edgecolor='black')
    
    plt.title("Wind Rose")
    plt.xlabel('Wind Direction')
    plt.ylabel('Wind Speed')
    plt.show()

# Histograms for GHI, DNI, DHI, WS, Tamb
def plot_histograms(df):
   
    columns = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    for column in columns:
        if column in df.columns:
            plot_histogram(df, column)

# Bubble Chart to explore complex relationships between GHI, Tamb, WS, and RH
def plot_bubble_chart(df, x_column='GHI', y_column='Tamb', size_column='WS', color_column='RH'):
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(df[x_column], df[y_column], s=df[size_column] * 10, c=df[color_column], cmap='viridis', alpha=0.5)
    plt.title(f'Bubble Chart of {x_column} vs {y_column} with WS and RH')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.colorbar(scatter, label=color_column)
    plt.show()
