import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    y_intercept = result.intercept

    extended_years = list(range(1880, 2051))

    plt.plot(extended_years, [y_intercept + slope * year for year in extended_years], 'r')

    # Create second line of best fit
    reduced_years = list(range(2000, 2051))

    reduced_result = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    reduced_slope = reduced_result.slope
    reduced_y_intercept = reduced_result.intercept

    plt.plot(reduced_years, [reduced_y_intercept + reduced_slope * year for year in reduced_years], 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()