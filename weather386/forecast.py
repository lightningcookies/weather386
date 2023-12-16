import requests
import pandas as pd

def get_forecast(lat, long):
    """
    Fetch forecast based on latitude and longitude from the NWS and returns
    it as a pandas DataFrame.

    Parameters:
    lat (float): Latitude
    long (float): Longitude

    Returns:
    pd.DataFrame: DataFrame containing the fetched data
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

        # Convert each one to a dataframe
        #df_temp = pd.DataFrame(forecast_grid_temp)
        #df_dewpoint = pd.DataFrame(forecast_grid_dewpoint)
        #df_maxTemperature = pd.DataFrame(forecast_grid_maxTemperature)
        #df_minTemperature = pd.DataFrame(forecast_grid_minTemperature)
        #df_relativeHumidity = pd.DataFrame(forecast_grid_relativeHumidity)
        #df_windDirection = pd.DataFrame(forecast_grid_windDirection)
        #df_windSpeed = pd.DataFrame(forecast_grid_windSpeed)
        #df_precip = pd.DataFrame(forecast_grid_precip)
        #df_snowfall = pd.DataFrame(forecast_grid_snowfallAmount)

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
    


#df_dict = get_forecast(40.76,-111.876)
#print(df_dict)
