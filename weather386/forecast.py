
import requests
import pandas as pd

def get_forecast(lat, long):
    """
    Fetch forecast based on latitude and longitude and return it as a pandas DataFrame.

    Parameters:
    lat (float): Latitude
    long (float): Longitude

    Returns:
    pd.DataFrame: DataFrame containing the fetched data
    """

    api_url = f"https://example.com/data?lat={lat}&long={long}"
    
    # Fetch data from the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data)
        return df
    else:
        # Handle errors or return an empty DataFrame
        return pd.DataFrame()
