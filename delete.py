from mongoengine import connect
from models import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = connect('ecobiciCDMX',
        host=f"mongodb+srv://{getenv('MONGO_USER')}:{getenv('MONGO_KEY')}@{getenv('MONGO_APP_NAME').lower()}.eelkqty.mongodb.net/?retryWrites=true&w=majority&appName={getenv('MONGO_APP_NAME')}")

Historico.objects.delete()