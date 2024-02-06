import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

from load_csv import load
import matplotlib.pyplot as plt


def preprocess(population):
    """
        string covert to float
    """
    if "M" in population:
        return float(population[:-1]) * 1e6
    elif "k" in population:
        return float(population[:-1]) * 1e3
    else:
        return float(population)

def plot_population_comparison(dataset: pd.DataFrame, campus: str, comparison_country: str):
    try:
        campus_data = dataset[dataset['country'] == campus].iloc[:, 1:].values.flatten()
        comparison_country_data = dataset[dataset['country'] == comparison_country].iloc[:, 1:]
        years = comparison_country_data.columns.astype(int)

        comparison_country_data = comparison_country_data.values.flatten()


        campus_pop = [preprocess(val) for val in campus_data]
        country_pop = [preprocess(val) for val in comparison_country_data]

        plt.plot(years, campus_pop, label=campus)
        plt.plot(years, country_pop, label=comparison_country)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1800, 2070)
        plt.ylabel("Population")
        plt.legend()
        plt.tight_layout()
        
        max_val = max(campus_pop + country_pop)
        y_ticks = [i * 1e7 for i in range(0, int(max_val / 1e7) + 1) if i % 2 == 0]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
        plt.show()



    except Exception as e:
        # Handle errors
        print(f"Error plotting data: {e}")

if __name__=='__main__':
    dataset = load("population_total.csv")
    if dataset is not None:
        # Specify your campus name and the country for comparison
        your_campus = "France" 
        comparison_country = "Russia"  
        plot_population_comparison(dataset, your_campus, comparison_country)


