import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def precip_graph(ax, historical_df, forecast_df):
    """
    Plots precipitation data comparing forecast data with historical data.

    This function takes a matplotlib Axes object and two DataFrames containing historical and forecasted
    precipitation data. It processes and visualizes the data as line plots, focusing on precipitation
    values across different hours of the day. The function aligns data by day-hour for direct comparison
    between the forecast and historical data.

    Parameters:
    ax (matplotlib.axes.Axes): The matplotlib Axes object to plot on. It should be pre-initialized.
    historical_df (pandas.DataFrame): A DataFrame containing historical weather data.
    forecast_df (pandas.DataFrame): A DataFrame containing forecast weather data.

    Returns:
    matplotlib.axes.Axes: The matplotlib Axes object with the plotted data.

    The function first standardizes the column names in both DataFrames. It then filters 
    the historical data to match the days present in the forecast data. The function plots 
    the precipitation data for each hour of the day, represented in the 'day_hour' column, 
    for the forecast data. Historical average precipitation is not plotted as it is often 
    unhelpful. The plot is customized with appropriate labels, a legend, and adjusted axis 
    limits. The x-axis represents 'Month-Day-Hour' in UTC, and the y-axis represents 
    precipitation in inches.
    """
    historical_df = historical_df.rename(columns={
        'date': 'validTime',
        'temperature_2m': 'temperature',
        'relative_humidity_2m': 'relativeHumidity',
        'dew_point_2m': 'dewpoint',
        'wind_speed_10m': 'windSpeed',
        'precipitation': 'precipitation' 
    })

    forecast_df['day_hour'] = forecast_df['validTime'].dt.strftime('%m-%d-%H')
    historical_df['day_hour'] = historical_df['validTime'].dt.strftime('%m-%d-%H')

    # Filter historical_df for unique days in forecast_df
    unique_days = forecast_df['validTime'].dt.strftime('%m-%d').unique()
    historical_df = historical_df[historical_df['validTime'].dt.strftime('%m-%d').isin(unique_days)]

    # Plotting
    sns.lineplot(x='day_hour', y='precipitation', data=forecast_df, errorbar=None, label='Forecast Precipitation', ax=ax)
    sns.lineplot(x='day_hour', y='precipitation', data=historical_df, errorbar='sd', label='Historical Average Precipitation', ax=ax)

    # Customize the plot
    ax.set_xlabel('Month-Day-Hour UTC time-zone')
    ax.set_ylabel('Precipitation IN')
    ax.set_title('Precipitation by Hour of the Day UTC')
    
    # Avoids lower sd band
    ax.set_ylim(bottom=-.0005)

    # Adjust x tick labels
    xticks = ax.get_xticks()
    xticklabels = [label.get_text() for label in ax.get_xticklabels()]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=45)

    # Reduce label frequency and set visibility
    for ind, label in enumerate(ax.get_xticklabels()):
        label.set_visible(ind % 4 == 0)
    ax.legend()

    # set x axis limit
    min_day_hour = forecast_df['day_hour'].min()
    max_day_hour = forecast_df['day_hour'].max()
    ax.set_xlim(min_day_hour, max_day_hour)
    return ax
