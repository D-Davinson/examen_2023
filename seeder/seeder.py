from pymongo import MongoClient
client = MongoClient(host="mongodb")

db = client["db_examen"]


col = db["col_examen"]

donnees_valides = {
    "titre": "Spring",
    "nom_artiste": "DDAVI",
    "immatriculation": "DD/260/RAP/1234",
    "type_musique": "RAP",
    "duration": 260
    }   

col.insert_one(donnees_valides)

print("Peuplement de la base de données terminé.")