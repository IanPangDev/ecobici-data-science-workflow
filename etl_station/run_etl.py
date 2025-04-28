from etl_station.extract import extract_data
from etl_station.transform import transform_data
from etl_station.load import load_data

def ETL_station():
    raw_data_info = extract_data()
    clean_data_info = transform_data(raw_data_info)
    load_data(clean_data_info)