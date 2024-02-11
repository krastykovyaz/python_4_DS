from load_csv import load_csv_dataset
import matplotlib.pyplot as plt

def visualize_life_expectancy_gdp_correlation():
    """
    Load 2 datasets and plot the correlation between Life Expectancy and Gross domestic product in 1900.
    """
    try:
        income_data = load_csv_dataset("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy_data = load_csv_dataset("life_expectancy_years.csv")
        
        if income_data is None or life_expectancy_data is None:
            raise ValueError("Failed to load dataset.")

        year_1900_column = '1900'
        gnp_1900 = income_data[year_1900_column]
        life_expectancy_1900 = life_expectancy_data[year_1900_column]

        plt.figure(figsize=(10, 6))
        plt.scatter(gnp_1900, life_expectancy_1900)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()
    except ValueError as error:
        print(f"Error: {error}")

def main():
    """
    Main function to visualize the correlation between life expectancy and GDP.
    """
    visualize_life_expectancy_gdp_correlation()

if __name__ == "__main__":
    main()
