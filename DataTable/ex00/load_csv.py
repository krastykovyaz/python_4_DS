import pandas as pd

def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the specified path and return it as a pandas DataFrame.

    Parameters:
        path (str): The path to the CSV file to be loaded.

    Returns:
        pd.DataFrame or None: The loaded dataset as a pandas DataFrame, or
        None if there was an error.

    This function loads a CSV dataset from the given path using the
    pandas library. It prints the dimensions of the loaded dataset
    and displays the first few rows of the dataset.
    If there is an error (e.g., bad path, bad format), None is returned.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        dataset = pd.read_csv(path)
        
        # Display the dimensions of the dataset
        print(f"Loading dataset of dimensions {dataset.shape}")

        # Display the first few rows of the dataset
        print(dataset.head())

        return dataset

    except Exception as e:
        # Handle errors and return None
        print(f"Error loading dataset: {e}")
        return None


def main():
    """
    Main function to load and display information about a dataset.
    """
    # Specify the path to the CSV file
    path = "your_dataset.csv"

    # Load the dataset
    dataset = load(path)

    # Perform further operations with the dataset if needed
    if dataset is not None:
        # Your additional code here
        pass
    else:
        print("Failed to load dataset.")

if __name__ == "__main__":
    main()
