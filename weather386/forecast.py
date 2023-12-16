import requests
import pandas as pd

def get_forecast(lat, long):
    """
    Retrieves weather forecast data for a specified latitude and longitude using the NWS API.

    This function sends a request to the National Weather Service (NWS) API and retrieves a variety
    of weather forecast data for the provided geographic coordinates. The data includes temperature,
    dewpoint, maximum and minimum temperatures, relative humidity, wind direction and speed,
    precipitation, and snowfall amounts. Each category of data is returned as a separate DataFrame
    within a dictionary.

    Parameters:
    lat (float): Latitude of the location for the weather forecast.
    long (float): Longitude of the location for the weather forecast.

    Returns:
    dict: A dictionary of pandas DataFrames, with keys representing different types of weather
          data ('temperature', 'dewpoint', 'maxTemperature', 'minTemperature', 'relativeHumidity',
          'windDirection', 'windSpeed', 'precipitation', 'snowfall'). Each DataFrame contains
          the respective forecast data.

    If the API request is unsuccessful, the function returns an empty dictionary. It's recommended
    to check the returned data for emptiness to handle any potential API request failures.
    """

    api_url = f"https://api.weather.gov/points/{lat},{long}"
    
    # Fetch data from the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        #FORECAST GRID DATA
        forecast_url = data['properties']['forecastGridData']
        g = requests.get(forecast_url)
        forecast_grid = g.json()

        # Grab all the data
        forecast_grid_temp = forecast_grid['properties']['temperature']['values']
        forecast_grid_dewpoint = forecast_grid['properties']['dewpoint']['values']
        forecast_grid_maxTemperature = forecast_grid['properties']['maxTemperature']['values']
        forecast_grid_minTemperature = forecast_grid['properties']['minTemperature']['values']
        forecast_grid_relativeHumidity = forecast_grid['properties']['relativeHumidity']['values']
        forecast_grid_windDirection = forecast_grid['properties']['windDirection']['values']
        forecast_grid_windSpeed = forecast_grid['properties']['windSpeed']['values']
        forecast_grid_precip = forecast_grid['properties']['quantitativePrecipitation']['values']
        forecast_grid_snowfallAmount = forecast_grid['properties']['snowfallAmount']['values']

        # list of dataframes
        dataframes = {
            'temperature': pd.DataFrame(forecast_grid_temp),
            'dewpoint': pd.DataFrame(forecast_grid_dewpoint),
            'maxTemperature': pd.DataFrame(forecast_grid_maxTemperature),
            'minTemperature': pd.DataFrame(forecast_grid_minTemperature),
            'relativeHumidity': pd.DataFrame(forecast_grid_relativeHumidity),
            'windDirection': pd.DataFrame(forecast_grid_windDirection),
            'windSpeed': pd.DataFrame(forecast_grid_windSpeed),
            'precipitation': pd.DataFrame(forecast_grid_precip),
            'snowfall': pd.DataFrame(forecast_grid_snowfallAmount)
        }
        return dataframes
    else:
        # Handle errors or return an empty DataFrame
        return {}