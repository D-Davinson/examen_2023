from fastapi import FastAPI
from pymongo import MongoClient
from Magasin_class import Magasin
from Musique_class import Musique

app = FastAPI()

client = MongoClient(host='mongodb')
db = client["db_examen"]
col = db["col_examen"]

@app.get("/magasin",response_model=list[Magasin])
def get_magasin():
    magasin = col.find()
    return list(magasin)

@app.post("/magasin", response_model=Magasin)
def create_magasin(magasin: Magasin):
    col.insert_one(magasin.model_dump()).inserted_id
    return magasin


@app.get("/musique",response_model=list[Musique])
def get_musique():
    musique = col.find()
    return list(musique)

@app.post("/musique", response_model=Musique)
def create_musique(musique:Musique):
    col.insert_one(musique.model_dump()).inserted_id
    return musique



