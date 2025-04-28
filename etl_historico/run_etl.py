from etl_historico.extract import extract_data
from etl_historico.transform import transform_data
from etl_historico.load import load_data
from os import listdir
from re import findall, search, sub, IGNORECASE
from tqdm import tqdm
from models import *

def get_files():
    folder = 'historico_csv\\'

    meses = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }
    fechas = {folder+i:findall(r'202[3|4][\_|\-][0-9a-z]+', i, IGNORECASE)[0] for i in listdir(folder)}
    
    convert_mes = lambda x: search(fr'{'|'.join(meses.keys())}', x, IGNORECASE)

    fechas = {clave:
        sub(rf'{convert_mes(valor).group()}', str(meses[convert_mes(valor).group()]), valor).replace('_', '-') if any([True for mes in meses.keys() if mes in valor]) else valor.replace('_', '-') for clave, valor in fechas.items()}
    
    return [i[0] for i in sorted(fechas.items(), key=lambda x: x[1])]

def ETL_historico():
    chunksize = 100_000
    
    for file in get_files():
        for raw_data_chunk in tqdm(extract_data(file, chunksize), desc="Segmento leido..."):
            clean_data_info = transform_data(raw_data_chunk)
            load_data(clean_data_info)