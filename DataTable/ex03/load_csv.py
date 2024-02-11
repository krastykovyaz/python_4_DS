import pandas as pd
import os

def load_csv_dataset(path: str) -> pd.DataFrame:
    """
    load csv and return pandas datasets
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("The specified file does not exist.")
        if not path.lower().endswith('.csv'):
            raise ValueError("Invalid file format. Expected .csv file.")
        dataset = pd.read_csv(path)
        print(f"Loading dataset from {path} with dimensions: {dataset.shape}")
        return dataset
    except (FileNotFoundError, ValueError) as error:
        print(f"Error loading dataset: {error}")
        return None
