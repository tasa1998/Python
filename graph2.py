from parser1 import Parser
from edge import Edge
import os
from vertex import Vertex
class Graph:
    def __init__(self):
        self.cvorovi = dict()
        self.grane = []
        self.listaReci = set()

    def insert_vertex(self, linkovi, reci, path):
        if path not in self.cvorovi.keys():
            cvorKojiDodajemo = Vertex(path, linkovi, reci)
            self.listaReci = self.listaReci.union(set(cvorKojiDodajemo.reci))
            self.cvorovi[path] = cvorKojiDodajemo

        for i in self.cvorovi[path].linkovi:
            if i in self.cvorovi.keys():
                self.cvorovi[i].veze.add(path)
            else:
                parserr = Parser()
                putanja = os.path.abspath(i)
                if putanja.startswith(path):
                    link, rec = parserr.parse(putanja)
                    cvor = Vertex(i, link, rec)
                    self.cvorovi[i] = cvor
                    self.cvorovi[i].veze.add(path)

            novaGrana = Edge(path, i)
            self.grane.append(novaGrana)


    """def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None: # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e"""