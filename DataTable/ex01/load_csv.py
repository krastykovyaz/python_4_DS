import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        # Read the CSV file into a pandas DataFrame
        dataset = pd.read_csv(path)
        
        # Display the dimensions of the dataset
        print(f"Loading dataset of dimensions {dataset.shape}")

        # Display the first few rows of the dataset

        return dataset

    except Exception as e:
        # Handle errors and return None
        print(f"Error loading dataset: {e}")
        return None


