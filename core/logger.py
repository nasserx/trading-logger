import pandas as pd
import os

def save_to_csv(file_name, headers, data):
    """
    Saves transaction data to a CSV file. 
    
    If the file does not exist or is empty, it creates the file and writes headers with the data.
    Otherwise, it appends the data without headers.
    
    Args:
        file_name (str): Path to the CSV file.
        headers (list): List of column headers.
        data (list): List of rows (each row is a list or tuple of values).
    """
    if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
        df = pd.DataFrame(data, columns=headers)
        df.to_csv(file_name, index=False, encoding='utf-8')
    else:
        df = pd.DataFrame(data)
        df.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8')
    
    print("✅ The transaction was saved successfully!")
