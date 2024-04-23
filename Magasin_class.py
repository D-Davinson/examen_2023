from pydantic import BaseModel
from Musique_class import Musique

class Magasin(BaseModel):
    type_magasin: str
    vynille_musique: list[Musique]
    dvd_musique: list[Musique]

    def ajouter_vynille_musique(self, musique : Musique):
        if self.type_magasin == musique.type_musique:
            self.vynille_musique.append(musique)
    def remove_vynille_musique(self, musique : Musique):
        self.vynille_musique.remove(musique)

    def ajouter_dvd_musique(self, musique : Musique):
        if self.type_magasin == musique.type_musique:
            self.dvd_musique.append(musique)
    def remove_dvd_musique(self, musique : Musique):
        self.dvd_musique.remove(musique)

        
