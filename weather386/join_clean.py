import pandas as pd
import numpy as np
from forecast import get_forecast
from expand import expand_df

def join_clean(df_dict):
    combined_df = None 
    for key, df in df_dict.items():
        # Expand each dataframe
        expanded_df = pd.concat([expand_df(row) for _, row in df.iterrows()], ignore_index=True)

        # Convert the 'value' column to Fahrenheit for temperature and dewpoint
        if key == 'temperature' or key == 'dewpoint' or key == 'maxTemperature' or key == 'minTemperature':
            expanded_df['value'] = expanded_df['value'] * 9/5 + 32

        expanded_df = expanded_df.rename(columns={'value': key})

        if combined_df is None:
            combined_df = expanded_df
        else:
            combined_df = pd.merge(combined_df, expanded_df, on='validTime', how='outer')
    return combined_df


x = get_forecast(40.76, -111.876)
combined_df = join_clean(x)
print(combined_df)
combined_df.to_csv('combined.csv')


