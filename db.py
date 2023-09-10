from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://rcastro86:gSNQLK4BFv4iOyd5@castroproyecto.4ivau6p.mongodb.net/?retryWrites=true&w=majority"
def cadena():
    try:
        # Cadena de conexión descargada de Mongo
        client = MongoClient(uri, server_api=ServerApi('1'))
        db=client['Libro']#Base de datos donde se almacenaran las busquedas
        client.admin.command('ping')
        print("Conexión Exitosa!")
        return db
    except exception as e:
        print("No se Pudo Conectar",e)

cadena()