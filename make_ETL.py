from etl_station import *
from etl_historico import *
from mongoengine import connect
from dotenv import load_dotenv
from os import getenv

if __name__ == '__main__':

    load_dotenv()

    client = connect('ecobiciCDMX',
        host=f"mongodb+srv://{getenv('MONGO_USER')}:{getenv('MONGO_KEY')}@{getenv('MONGO_APP_NAME').lower()}.eelkqty.mongodb.net/?retryWrites=true&w=majority&appName={getenv('MONGO_APP_NAME')}")
    
    print('\nEntrando al ETL de las estaciones')
    ETL_station()

    print('\nEntrando al ETL del historico')
    ETL_historico()

    print('Proceso terminado')
    client.close()