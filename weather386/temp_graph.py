import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def temp_graph(ax, historical_df, forecast_df):
    """
    Plots temperature data comparing historical averages with forecast data.

    This function takes two dataframes containing historical and forecasted temperature data,
    along with an Axes object for plotting. It processes the data to align by day-hour
    and plots both historical and forecasted temperature data on the same graph.

    Parameters:
    ax (matplotlib.axes.Axes): The matplotlib Axes object to plot on.
    historical_df (pandas.DataFrame): Dataframe containing historical temperature data.
    forecast_df (pandas.DataFrame): Dataframe containing forecasted temperature data.

    Returns:
    matplotlib.axes.Axes: The matplotlib Axes object with the plotted data.
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
    sns.lineplot(x='day_hour', y='temperature', data=forecast_df, errorbar=None, label='Forecast Temperature', ax=ax)
    sns.lineplot(x='day_hour', y='temperature', data=historical_df, errorbar='sd', label='Historical Average Temperature', ax=ax)

    # Customize the plot
    ax.set_xlabel('Month-Day-Hour UTC time-zone')
    ax.set_ylabel('Temperature F')
    ax.set_title('Temperature by Hour of the Day UTC')

    # Adjust x tick labels
    xticks = ax.get_xticks()
    xticklabels = [label.get_text() for label in ax.get_xticklabels()]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=45)

    # Reduce label frequency and set visibility
    for ind, label in enumerate(ax.get_xticklabels()):
        label.set_visible(ind % 4 == 0)
    # Set x axis limit
    min_day_hour = forecast_df['day_hour'].min()
    max_day_hour = forecast_df['day_hour'].max()
    ax.set_xlim(min_day_hour, max_day_hour)

    ax.legend()
    return ax

