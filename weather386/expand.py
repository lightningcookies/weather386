from dateutil.parser import parse
import pandas as pd

def expand_df(row):
    start_time = pd.to_datetime(row['validTime'].split('/')[0])
    duration_hours = int(row['validTime'].split('PT')[-1].split('H')[0])
    end_time = start_time + pd.Timedelta(hours=duration_hours)

    return pd.DataFrame({
    'validTime': pd.date_range(start=start_time, end=end_time, freq='H', inclusive='left'),
    'value': row['value']
    })