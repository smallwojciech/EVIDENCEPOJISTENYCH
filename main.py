from pojistenec import Pojistenec
from evidence import EvidencePojistenych
from uzivatelske_rozhrani import UzivatelskeRozhrani
from validace import Validator  

evidence = EvidencePojistenych()
validace = Validator(evidence)
rozhrani = UzivatelskeRozhrani(evidence, validace)


UzivatelskeRozhrani.aplikace(rozhrani)


