import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def plot_campus_life_expectancy(dataset: pd.DataFrame, campus: str):
    """
    Plot life expectancy projections for a given campus.

    Args:
        dataset (pd.DataFrame): DataFrame containing life expectancy data.
        campus (str): Name of the campus to plot.

    Returns:
        None: Displays the plot.

    This function plots the life expectancy projections over the years for a given campus.
    """
    try:
        # Filter data for the specified campus
        campus_data = dataset[dataset['country'] == campus]

        # Extract years and life expectancy values
        years = campus_data.columns[1:]
        life_expectancy = campus_data.iloc[:, 1:].values.flatten()

        # Create a line plot
        plt.plot(years, life_expectancy, label=campus)
        plt.xticks(years[::40])
        plt.yticks(range(30, 100, 10))
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(f'{campus} Life expectancy Projections')
        plt.show()

    except Exception as e:
        # Handle errors
        print(f"Error plotting data: {e}")

def main():
    """
    Main function to plot life expectancy projections.
    """
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        your_campus = "France"  # Replace with the actual campus name
        plot_campus_life_expectancy(dataset, your_campus)

if __name__ == "__main__":
    main()
