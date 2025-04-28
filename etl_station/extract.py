import requests

def extract_data():
    url_station_info = 'https://gbfs.mex.lyftbikes.com/gbfs/en/station_information.json'
    return requests.get(url_station_info).json()