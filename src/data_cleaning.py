
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


def handle_outliers(df, columns, method='remove', threshold=3):
    
    if method == 'remove':
        
        for column in columns:
            z_scores = (df[column] - df[column].mean()) / df[column].std()
            df = df[z_scores.abs() <= threshold]  
    elif method == 'cap':
        
        for column in columns:
            z_scores = (df[column] - df[column].mean()) / df[column].std()
            lower_limit = df[column].mean() - threshold * df[column].std()
            upper_limit = df[column].mean() + threshold * df[column].std()
            df[column] = np.where(df[column] < lower_limit, lower_limit, df[column])
            df[column] = np.where(df[column] > upper_limit, upper_limit, df[column])
    
    return df

        