import pandas as pd

def extract_data(file, chunksize):
    return pd.read_csv(file, chunksize=chunksize)