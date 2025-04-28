from models import *
from tqdm import tqdm

def load_data(clean_data_info):
    stations = StationInformation.objects().aggregate([
        {
            '$project': {
                '_id': 0,
                'station_id': 1
            }
        }
    ])

    stations = set([i['station_id'] for i in stations])

    for document in tqdm(clean_data_info, desc="Documento leido..."):
        if document['station_id'] not in stations:
            document.save()