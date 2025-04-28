from models import *
import pandas as pd

def format_stations(raw_data):
    # Quitando la primera estacion, nos quedamos la segunda
    # Quitando el cero inicial de id estacion
    raw_data['Ciclo_Estacion_Retiro'] = raw_data['Ciclo_Estacion_Retiro'].str.replace(r'[ 0-9]+\-[ ]?|^0+', '', regex=True)
    raw_data['Ciclo_EstacionArribo'] = raw_data['Ciclo_EstacionArribo'].str.replace(r'[ 0-9]+\-[ ]?|^0+','', regex=True)

def format_date(raw_data):
    # Formato de fecha
    raw_data['Fecha_Retiro'] = pd.to_datetime(raw_data['Fecha_Retiro'], format='%d/%m/%Y')
    raw_data['Hora_Retiro'] = pd.to_timedelta(raw_data['Hora_Retiro'])
    raw_data['Fecha_Arribo'] = pd.to_datetime(raw_data['Fecha_Arribo'], format='%d/%m/%Y')
    raw_data['Hora_Arribo'] = pd.to_timedelta(raw_data['Hora_Arribo'])
    
    # Uniendo fecha y hora
    raw_data['Fecha_retiro_unificada'] = raw_data['Fecha_Retiro']+raw_data['Hora_Retiro']
    raw_data['Fecha_arribo_unificada'] = raw_data['Fecha_Arribo']+raw_data['Hora_Arribo']

    #Dandole formato a la fecha
    raw_data['Fecha_retiro_unificada'] = raw_data['Fecha_retiro_unificada'].astype(str).str.replace(' ', 'T')
    raw_data['Fecha_arribo_unificada'] = raw_data['Fecha_arribo_unificada'].astype(str).str.replace(' ', 'T')

def format_gender(raw_data):
    raw_data['Genero_Usuario'] = raw_data['Genero_Usuario'].apply(lambda x: 'Sin_definir' if x not in ['M', 'F'] else x)

def remove_nan(raw_data):
    # Remplazando datos vacios
    raw_data['Genero_Usuario'] = raw_data['Genero_Usuario'].fillna('None').astype(str)
    raw_data['Edad_Usuario'] = raw_data['Edad_Usuario'].fillna(0).astype(int)

def transform_data(raw_data):
    
    remove_nan(raw_data)

    format_date(raw_data)
    
    format_stations(raw_data)

    format_gender(raw_data)
    

    documents = []
    for _, row in raw_data.iterrows():
        documents.append(Historico(
            usuario=Usuario(
                genero = row['Genero_Usuario'],
                edad = row['Edad_Usuario']
            ),
            viaje=Viaje(
                estacion_retiro = row['Ciclo_Estacion_Retiro'],
                fecha_retiro = row['Fecha_retiro_unificada'],
                estacion_arribo = row['Ciclo_EstacionArribo'],
                fecha_arribo = row['Fecha_arribo_unificada']
            )
        ))

    return documents