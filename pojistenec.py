

class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon,druh_pojisteni, narodnost):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        self.druh_pojisteni = druh_pojisteni
        self.narodnost = narodnost

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon} {self.druh_pojisteni} {self.narodnost}"
    

