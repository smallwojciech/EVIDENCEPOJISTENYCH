from pojistenec import Pojistenec
from evidence import EvidencePojistenych
from uzivatelske_rozhrani import UzivatelskeRozhrani

evidence = EvidencePojistenych()
rozhrani = UzivatelskeRozhrani(evidence)


UzivatelskeRozhrani.aplikace(rozhrani)


