from graph2 import Graph
from parser1 import Parser
import os


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
    print("Unesite direktorijum koji zelite da parsirate: ")

    while True:
        print("Breakpoint")
        root = os.path.abspath(os.getcwd())
        direktorijum = input()
        root = os.path.join(root, direktorijum)
        graf = napraviGraf(root)
        print("Proslo")


