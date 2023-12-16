import matplotlib.pyplot as plt
import pandas as pd
from weather386.precip_graph import precip_graph
from weather386.temp_graph import temp_graph
from weather386.wind_graph import wind_graph

def combined_graph(historical_df,forecast_df):
    """
    Creates a combined plot with separate graphs for precipitation, temperature, and wind speed.

    This function takes historical and forecasted weather data and plots three separate graphs 
    on a single figure. Each graph represents a different aspect of the weather data: precipitation, 
    temperature, and wind speed. The function utilizes specific graphing functions from the 
    'weather386' module for each of these aspects.

    Parameters:
    historical_df (pandas.DataFrame): A DataFrame containing historical weather data.
                                      Required columns include 'precipitation', 'windSpeed',
                                      and 'temperature'.
    forecast_df (pandas.DataFrame): A DataFrame containing forecasted weather data.
                                    Required columns are the same as for historical_df.

    The function creates a figure with three subplots arranged vertically. It then calls the
    precip_graph, temp_graph, and wind_graph functions from the 'weather386' module, passing 
    each a subplot Axes object along with the historical and forecasted DataFrames. The function 
    adjusts the layout for better readability and displays the combined plot.

    Note:
    This function relies on the 'weather386' module's specific graphing functions. It assumes 
    these functions are correctly implemented and available.
    """
    
    fig, axs = plt.subplots(3,1, figsize=(15,10))
    precip_graph(axs[0], historical_df, forecast_df)
    temp_graph(axs[1], historical_df, forecast_df)
    wind_graph(axs[2], historical_df, forecast_df)
    plt.subplots_adjust(hspace=0.4)
    plt.tight_layout()
    plt.show()
