from pydantic import BaseModel, field_validator

class Musique(BaseModel):
    titre: str
    nom_artiste: str
    immatriculation: str
    type_musique: str
    duration: int


    @field_validator('type_musique')
    def check_type_musique(cls, type):
        if type not in ['RAP','POP','RNB']:
            raise ValueError("type doit être RAP,POR ou RNB")
        return type

    @field_validator('immatriculation')
    def check_immatriculation(cls, immatric, value):
        if len(immatric)!= 15:
            raise ValueError("Err -> immatricule doit être de 15 characters")
        if immatric[0].upper() != value["nom_artiste"][0].upper() or immatric[1].upper() != value["nom_artiste"][1].upper():
            raise ValueError("Err -> immatricule doit  commencer par les deux premier initial de l'artise")
        if int(immatric[3,4,5]) < 60 or int(immatric[3,4,5]) > 300:
            raise ValueError("Err -> immatricule doit avoir une durée entre 1min et 5min")
        if immatric[7,8,9] not in ['RAP','POP','RNB']:
            raise ValueError("Err -> immatricule doit être RAP,POR ou RNB")
        if '6' in immatric[10,11,12,13,14]:
            raise ValueError("Err -> immatricule doit pas contenir le chiffre 6")
        if immatric[2] != '/' or immatric[6] != '/' or immatric[10] != '/':
            raise ValueError("Err -> immatricule à une mauvaise forme :(")
        return immatric


