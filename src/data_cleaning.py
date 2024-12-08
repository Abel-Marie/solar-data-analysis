# src/data_cleaning.py
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    

def check_missing_values(df):
    
    missing_values = df.isnull().sum()
    missing_percentage = (df.isnull().mean()) * 100
    missing_info = pd.DataFrame({
        'Missing Values': missing_values,
        'Percentage': missing_percentage
    })
    return missing_info


def check_duplicates(df):
 
    duplicates = df.duplicated().sum()
    return duplicates


def check_negative_values(df, columns):
   
    negative_values = {}
    for column in columns:
        if column in df.columns:
            negative_values[column] = (df[column] < 0).sum()
        else:
            negative_values[column] = None  

    negative_values_df = pd.DataFrame(list(negative_values.items()), columns=['Column', 'Negative Count'])
    return negative_values_df




def clean_missing_values(df, strategy='mean'):
    """
    Handle missing values in the DataFrame by filling them.
    Options for strategy: 'mean', 'median', 'mode', 'drop'.
    """
    if strategy == 'mean':
        df.fillna(df.mean(), inplace=True)
    elif strategy == 'median':
        df.fillna(df.median(), inplace=True)
    elif strategy == 'mode':
        df.fillna(df.mode().iloc[0], inplace=True)
    elif strategy == 'drop':
        df.dropna(inplace=True)
    else:
        print(f"Unknown strategy: {strategy}")
    
    return df

def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """
    df.drop_duplicates(inplace=True)
    return df

def convert_columns_to_datetime(df, date_columns):
    """
    Convert specified columns to datetime format.
    :param df: The DataFrame containing the data.
    :param date_columns: List of column names that should be converted to datetime.
    """
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            print(f"Column {col} converted to datetime.")
    return df

def normalize_columns(df, columns):
    """
    Normalize the specified columns (min-max scaling).
    :param df: The DataFrame containing the data.
    :param columns: List of column names to normalize.
    """
    for col in columns:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            df[col] = (df[col] - min_val) / (max_val - min_val)
            print(f"Column {col} normalized.")
    return df
