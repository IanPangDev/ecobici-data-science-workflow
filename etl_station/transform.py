from models import *

def transform_data(raw_data_info):
    new_stationInformation = [
        StationInformation(
            station_id=i['station_id'],
            name=i['name'],
            coords=[float(i['lon']), float(i['lat'])],
            capacity=int(i['capacity'])
        )
        for i in raw_data_info['data']['stations']]

    return new_stationInformation