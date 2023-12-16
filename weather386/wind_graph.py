import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def wind_graph(ax, historical_df, forecast_df):
    """
    Creates a line plot comparing historical and forecasted wind speed data.

    This function generates a plot on a provided Axes object, displaying wind speed data from 
    both historical and forecasted sources. It aligns data by the hour of the day (UTC) for 
    comparison and visualizes it using line plots.

    Parameters:
    ax (matplotlib.axes.Axes): The matplotlib Axes object to plot on. It should be pre-initialized.
    historical_df (pandas.DataFrame): A DataFrame containing historical weather data.
    forecast_df (pandas.DataFrame): A DataFrame containing forecast weather data.

    Returns:
    matplotlib.axes.Axes: The matplotlib Axes object with the plotted data.

    The function first standardizes the column names in both DataFrames and then filters 
    the historical data to match the days present in the forecast data. It plots the wind 
    speed ('windSpeed') for each hour of the day, represented in the 'day_hour' column, 
    for both historical and forecast data. The plot is customized with appropriate labels 
    and a legend. The x-axis represents 'Month-Day-Hour' in UTC, and the y-axis represents 
    wind speed in miles per hour (MPH).
    """
    historical_df = historical_df.rename(columns={
        'date': 'validTime',
        'temperature_2m': 'temperature',
        'relative_humidity_2m': 'relativeHumidity',
        'dew_point_2m': 'dewpoint',
        'wind_speed_10m': 'windSpeed'
    })
    forecast_df['day_hour'] = forecast_df['validTime'].dt.strftime('%m-%d-%H')
    historical_df['day_hour'] = historical_df['validTime'].dt.strftime('%m-%d-%H')

    # Filter historical_df for unique days in forecast_df
    unique_days = forecast_df['validTime'].dt.strftime('%m-%d').unique()
    historical_df = historical_df[historical_df['validTime'].dt.strftime('%m-%d').isin(unique_days)]

    # Plotting
    sns.lineplot(x='day_hour', y='windSpeed', data=forecast_df, errorbar=None, label='Forecast', ax=ax)
    sns.lineplot(x='day_hour', y='windSpeed', data=historical_df, errorbar='sd', label='Historical Average', ax=ax)

    # Customize the plot
    ax.set_xlabel('Month-Day-Hour UTC time-zone')
    ax.set_ylabel('Wind Speed MPH')
    ax.set_title('Wind Speed by Hour of the Day UTC')

    xticks = ax.get_xticks()
    xticklabels = [label.get_text() for label in ax.get_xticklabels()]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=45)

    # Reduce label frequency and set visibility
    for ind, label in enumerate(ax.get_xticklabels()):
        label.set_visible(ind % 4 == 0)
    
    ax.legend()
    # Set x axis limit
    min_day_hour = forecast_df['day_hour'].min()
    max_day_hour = forecast_df['day_hour'].max()
    ax.set_xlim(min_day_hour, max_day_hour)

    return ax
