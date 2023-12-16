import pandas as pd
import numpy as np
from weather386.expand import expand_df

def join_clean(df_dict):
    """
    Joins and cleans multiple weather data DataFrames.

    This function takes a dictionary of DataFrames, each representing a different type of weather data,
    and combines them into a single DataFrame. It performs expansion of each DataFrame, conversion of
    temperature values to Fahrenheit (where applicable), and then merges them on a common time column.

    Parameters:
    df_dict (dict): A dictionary where keys are strings representing the type of weather data 
                    (e.g., 'temperature', 'dewpoint', 'precipitation', 'windSpeed') and values 
                    are pandas DataFrames containing the corresponding data.

    Returns:
    pandas.DataFrame: A combined DataFrame with each weather data type as a column, aligned by the
                      'validTime' column. Temperature and dewpoint values are converted to Fahrenheit.
                      precipitation is converted from mm to in.

    Each DataFrame in the input dictionary is first expanded using the `expand_df` function. Then, for
    DataFrames representing temperature or dewpoint, values are converted from Celsius to Fahrenheit. Then,
    for the precipitation DataFrame, values are converted to inches from millimeters.
    The DataFrames are then merged into a single DataFrame on the 'validTime' column. If the 'validTime'
    column does not exist in any of the DataFrames, the merge may not align the data correctly.
    """
    combined_df = None 
    for key, df in df_dict.items():
        # Expand each dataframe
        expanded_df = pd.concat([expand_df(row) for _, row in df.iterrows()], ignore_index=True)

        if key == 'temperature' or key == 'dewpoint' or key == 'maxTemperature' or key == 'minTemperature':
            expanded_df['value'] = expanded_df['value'] * 9/5 + 32
        
        if key == 'precipitation':
            expanded_df['value'] = expanded_df['value'] / 25.4

        expanded_df = expanded_df.rename(columns={'value': key})

        if combined_df is None:
            combined_df = expanded_df
        else:
            combined_df = pd.merge(combined_df, expanded_df, on='validTime', how='outer')
    return combined_df