from evidence import EvidencePojistenych
from pojistenec import Pojistenec

class UzivatelskeRozhrani:
    def __init__(self, evidence: EvidencePojistenych):
        self.evidence = evidence

    def vypis_menu(self):
        while True:
            print("---------------------------")
            print("Evidence pojištěných")
            print("---------------------------")
            print("Vyber akci:")
            print("1 - Přidat nového pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojištěného")
            print("4 - Konec")

            task = input().strip()

            if task == "1":
                jmeno = input("Zadej jméno: ").strip()
                prijmeni = input("Zadej příjmení: ").strip()
                vek = input("Zadej věk: ").strip()
                telefon = input("Zadej telefonní číslo: ").strip()
                druh_pojisteni = input("Zadej druh pojištění: ").strip()
                narodnost = input("Zadej národnost: ").strip()

                novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon, druh_pojisteni, narodnost)
                self.evidence.pridat_pojistence(novy_pojistenec)
                print("Pojištěný byl přidán.\n")

            elif task == "2":
                self.evidence.vypsat_pojistence()
                print()

            elif task == "3":
                jmeno = input("Zadej jméno pojištěného: ").strip()
                if not jmeno:
                    print("Jméno nesmí být prázdné.\n")
                    continue
                prijmeni = input("Zadej příjmení pojištěného: ").strip()
                if not prijmeni:
                    print("Příjmení nesmí být prázdné.\n")
                    continue
                druh_pojisteni = input("Zadej druh pojištění: ").strip()

                self.evidence.vyhledat_pojistence(jmeno, prijmeni, druh_pojisteni)
                print()

            elif task == "4":
                
                break

            else:
                print("Neplatná volba, zkus to znovu.\n")

    def aplikace(self):
        self.vypis_menu()
