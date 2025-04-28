import mongoengine as db

class Usuario(db.EmbeddedDocument):
    genero = db.StringField(required=True)
    edad = db.IntField(required=True)

class Viaje(db.EmbeddedDocument):
    estacion_retiro = db.StringField(required=True)
    fecha_retiro = db.DateTimeField(required=True)
    estacion_arribo = db.StringField(required=True)
    fecha_arribo = db.DateTimeField(required=True)


class Historico(db.Document):
    usuario = db.EmbeddedDocumentField(Usuario, required=True)
    viaje = db.EmbeddedDocumentField(Viaje, required=True)
    
    meta = {
        'collection': 'historico'
    }