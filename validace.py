from evidence import EvidencePojistenych
from pojistenec import Pojistenec


class Validator:
    def __init__(self, evidence):
        self.evidence = evidence

    def jmeno_je_validni(self, jmeno):
        if jmeno.isalpha() and len(jmeno) > 0:
            return True
        
    
    def prijmeni_je_validni(self, prijmeni):
        if prijmeni.isalpha() and len(prijmeni) > 0:
            return True
        
            

    def vek_je_validni(self, vek):
        if vek.isdigit() and 0 < int(vek) < 80:
            return True
        