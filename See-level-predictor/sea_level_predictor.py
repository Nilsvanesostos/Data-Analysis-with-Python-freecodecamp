import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=20, c='b')

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = np.arange(1880, 2050, 1)
    plt.plot(x, intercept + x * slope, color="red")

    # Create second line of best fit
    dfSinceY2K = df[df["Year"] >= 2000]
    slope, intercept, r_value, p_value, stderr = linregress(dfSinceY2K["Year"], dfSinceY2K["CSIRO Adjusted Sea Level"])
    x = np.arange(1880, 2050, 1)
    plt.plot(x, intercept + x * slope, color="green")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()