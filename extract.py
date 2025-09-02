import pandas as pd
import os

def extract_data(file_path="data/raw_customers.csv"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
        print(f"Data extracted: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        raise