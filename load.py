import pandas as pd
import os

def load_data(df: pd.DataFrame, output_path="data/processed_customers.csv") -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        df.to_csv(output_path, index=False)
        print(f"Transformed data saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
        raise