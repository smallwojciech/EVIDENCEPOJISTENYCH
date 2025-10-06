class EvidencePojistenych:
    def __init__(self):
        self.pojistenci = []

    def pridat_pojistence(self, pojistenec):
        self.pojistenci.append(pojistenec)

    def vrat_pojistence(self):
        return self.pojistenci
    
    def vypsat_pojistence(self):
        if not self.pojistenci:
            print("Žádní pojištění nejsou evidováni.")
        else:
            for pojistenec in sorted(self.pojistenci, key=lambda p: p.jmeno):
                print(pojistenec)

    def vyhledat_pojistence(self, jmeno, prijmeni, druh_pojisteni):
        nalezeni_pojistenci = [
            pojistenec for pojistenec in self.pojistenci
            if pojistenec.jmeno.lower() == jmeno.lower() and
               pojistenec.prijmeni.lower() == prijmeni.lower() and
               (not druh_pojisteni or pojistenec.druh_pojisteni.lower() == druh_pojisteni.lower())
        ]

        if not nalezeni_pojistenci:
            print("Pojištěný nebyl nalezen.")
        else:
            for pojistenec in nalezeni_pojistenci:
                print(pojistenec)