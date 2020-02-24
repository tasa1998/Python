from graph2 import Graph
from parser1 import Parser
import os
from set import Set

"""brojevi = Set()
brojevi.dodaj(1)
brojevi.dodaj(2)
brojevi1 = Set()
brojevi1.dodaj(2)
brojevi1.dodaj(4)

brojevi.presek(brojevi1)
resenje = Set()
resenje = brojevi.presek(brojevi1)
resenje.ispisi()"""

def napraviGraf(path):
    graf=Graph()
    parserr=Parser()
    for koren,folderi,datoteke in os.walk(path):
        for ime in datoteke:
            if ime.endswith(".html"):
                filepath = os.path.join(koren,ime)
                linkovi, reci=parserr.parse(filepath)
                graf.insert_vertex(linkovi, reci, filepath)
    return graf

if __name__ == "__main__":
    print("Unesite direktorijum: ")

    while True:
        root = os.path.abspath(os.getcwd())
        direktorijum = input()
        while (not os.path.isdir(direktorijum)):
            print("Ne postoji uneti direktorijum")
            direktorijum = input()
        root = os.path.join(root, direktorijum)
        graf = napraviGraf(root)
        print("Proslo")


