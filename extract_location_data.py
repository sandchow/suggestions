import pandas as pd
import requests


def get_location(latitude, longitude):
    r = requests.get('https://nominatim.openstreetmap.org/reverse', params={
        'lat': latitude,
        'lon': longitude,
        'format': 'json',
    })
    return r.json()


def get_suggestion(data):
    data_new = data.apply(lambda x: get_location(x['latitude'], x['longitude']), axis=1)
    data_new.to_json('sample_data.json')


if __name__ == '__main__':
    path = 'data/'
    for file_name in ['1']:
        df = pd.read_csv(path + file_name + '.csv')
        df.columns = ['timestamp', 'latitude', 'longitude']
        df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
        get_suggestion(df.iloc[1:3])

