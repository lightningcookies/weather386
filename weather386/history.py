import requests
import pandas as pd

def get_history(lat,long,start_date):
    """
    Fetch historical weather data for a specific location and time period.

    This function retrieves historical weather data, including maximum and minimum temperatures, 
    total precipitation, rain and snowfall sums, and maximum wind speeds, from a specified start date 
    to the fixed end date of '2023-11-19'. The data is fetched from the Open-Meteo API and returned 
    as a pandas DataFrame.

    Parameters:
    lat (float): Latitude of the location for which to fetch weather data.
    long (float): Longitude of the location for which to fetch weather data.
    start_date (str): The start date for the historical data retrieval in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: A DataFrame containing the daily weather data for the specified period. 
                      The DataFrame includes columns for maximum and minimum temperatures 
                      (in Fahrenheit), total precipitation (in inches), rain and snowfall sums,
                      and maximum wind speeds (in mph).

    Example:
    >>> df = get_history(39.7392, -104.9903, '1950-01-01')
    >>> df.head()
    """

    #start_date = '1950-11-15'
    end_date = '2023-11-19'
    daily_parameters = 'temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,snowfall_sum,wind_speed_10m_max,wind_gusts_10m_max'
    temperature_unit = 'fahrenheit'
    wind_speed_unit = 'mph'
    precipitation_unit = 'inch'
    timezone = 'GMT'

    # Construct URL using f-string
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={long}&start_date={start_date}&end_date={end_date}&daily={daily_parameters}&temperature_unit={temperature_unit}&wind_speed_unit={wind_speed_unit}&precipitation_unit={precipitation_unit}&timezone={timezone}"
    
    # Request data
    x = requests.get(url)
    data = x.json()

    #df creation
    daily_data = data['daily']
    df = pd.DataFrame(daily_data)
    return df

history_df = get_history(40.76,-111.876,'1950-11-15')
history_df.to_csv('history_slc.csv')