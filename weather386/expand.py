from dateutil.parser import parse
import pandas as pd

def expand_df(row):
    """
    Expands a single row of weather data into a DataFrame with hourly records.

    This function takes a row from a DataFrame representing a single weather data record and 
    expands it into a DataFrame with hourly intervals. It is particularly useful for expanding 
    weather data that spans multiple hours into individual hourly records.

    Parameters:
    row (pandas.Series): A row from a DataFrame, expected to contain the columns 'validTime' and 'value'.
                         The 'validTime' field should be a string in the format "YYYY-MM-DDTHH:MM/PTnH",
                         where 'n' is the duration in hours.

    Returns:
    pandas.DataFrame: A DataFrame with two columns: 'validTime' and 'value'. The 'validTime' column
                      contains a range of datetime objects at hourly intervals, starting from the
                      start time specified in the input row and continuing for the duration specified.
                      The 'value' column is filled with the value from the input row.

    The function parses the 'validTime' field to extract the start time and duration, then creates a
    range of datetime objects at hourly intervals. Each datetime object corresponds to a separate row
    in the returned DataFrame, and the 'value' column in each row is filled with the value from the
    input row.
    """
    start_time = pd.to_datetime(row['validTime'].split('/')[0])
    duration_hours = int(row['validTime'].split('PT')[-1].split('H')[0])
    end_time = start_time + pd.Timedelta(hours=duration_hours)

    return pd.DataFrame({
    'validTime': pd.date_range(start=start_time, end=end_time, freq='H', inclusive='left'),
    'value': row['value']
    })