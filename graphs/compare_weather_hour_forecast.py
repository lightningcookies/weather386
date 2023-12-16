def compare_weather_hour_forecast(historical_df, forecast_df, date_column, value_column, target_date):
    """
    Compare historical weather data with the current forecast using a graph with a confidence interval.

    Parameters:
    - historical_df: DataFrame containing historical weather data.
    - forecast_df: DataFrame containing the current weather forecast data.
    - date_column: Name of the column in both DataFrames containing the date information.
    - value_column: Name of the column in both DataFrames containing the weather variable to compare.
    - target_date: Date in the format 'MM-DD' to filter the data.

    Returns:
    - None (the function will display the graph).
    """
    # Clean data and merge the two DataFrames on the date_column
    historical_df = historical_df.rename(columns={
        'date': 'validTime',
        'temperature_2m': 'temperature',
        'relative_humidity_2m': 'relativeHumidity',
        'dew_point_2m': 'dewpoint',
        'wind_speed_10m': 'windSpeed'
    })
    columns_to_drop = ['rain', 'Unnamed: 0']
    historical_data = historical_df.drop(columns=columns_to_drop, errors='ignore')
    historical_df['date'] = historical_df['validTime'].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime("%m-%d")
    )
    
    columns_to_drop = ['windDirection', 'Unnamed: 0', 'minTemperature', 'maxTemperature']
    forecast_df = forecast_df.drop(columns=columns_to_drop, errors='ignore')
    forecast_df['date'] = forecast_df['validTime'].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S%z").strftime("%m-%d")
    )

    # Filter data for the target date
    historical_df = historical_df[historical_df['date'] == target_date]
    forecast_df = forecast_df[forecast_df['date'] == target_date]

    # Extract hour from the validTime columns
    historical_df['hour'] = pd.to_datetime(historical_df['validTime']).dt.hour
    forecast_df['hour'] = pd.to_datetime(forecast_df['validTime']).dt.hour

    merged_df = pd.merge(historical_df, forecast_df, on=['date', 'hour'], suffixes=('_historical', '_forecast'))

    sns.lineplot(x=merged_df['hour'], y=merged_df[value_column + '_historical'], label='Historical', ci=None, color='blue')

    # Add confidence interval around the historical line
    sns.lineplot(x=merged_df['hour'], y=merged_df[value_column + '_historical'], ci='sd', color='blue', alpha=0.2)

    # Plot the smooth line for forecast data
    sns.lineplot(x=merged_df['hour'], y=merged_df[value_column + '_forecast'], label='Forecast', ci='sd', color='red')

    # Set plot labels and title
    plt.xlabel('Hour of the Day')
    plt.ylabel(value_column)
    plt.title(f'Comparison of Historical Data and Forecast for {value_column} on {target_date}')

    # Show legend
    plt.legend()

    # Show the plot
    plt.show()

# Example usage:
# historical_data = pd.read_csv('historical_weather.csv')
# forecast_data = pd.read_csv('forecast_weather.csv')
# compare_weather_day_forecast(historical_data, forecast_data, 'date', 'temperature', '12-11')
