from src.text.parser import Parser
from src.structure.edge import Edge
import os
from src.structure.vertex import Vertex

class Graph:
    def __init__(self):
        self.cvorovi = dict()           #sve cvorove smestam u recnik
        #self.grane = []                #cuvala sam i linkove na koje pokazuje i reci koje sadrzi odredjena putanja, ali to vec imam u cvoru
        #self.listaReci = Set()

    def insert_vertex(self, linkovi, reci, path):       #uzimam datu putanju i smestam je u cvor ukoliko ne postoji, napravim novi i dodam ga, a kljuc ce mi biti ta ista putanja
        if path not in self.cvorovi.keys():
            cvorKojiDodajemo = Vertex(path, linkovi, reci)
            #self.listaReci = self.listaReci.union(set(cvorKojiDodajemo.reci))
            self.cvorovi[path] = cvorKojiDodajemo

        for i in self.cvorovi[path].linkovi:            #prolazim kroz linkove koje putanja sadrzi i koje sam smestila u cvor
            if i in self.cvorovi.keys():                #ako se link nalazi u tom cvoru dodajem ga u skup veza i cuvam ga tamo
                self.cvorovi[i].veze.dodaj(path)
            else:
                parserr = Parser()                      
                putanja = os.path.abspath(i)            #uzimam putanju linka
                if putanja.startswith(path):            #ako putanja pocinje putanjom cvora koji sam vec napravila
                    link, rec = parserr.parse(putanja)  #parsiram putanju da bi dobila linkove i reci koje ona sadrzi
                    cvor = Vertex(i, link, rec)         #pravim novi cvor sa tim linkom i tako za svaki link u putanji koja je uneta
                    self.cvorovi[i] = cvor               #dodajem ga u listu cvorova
                    self.cvorovi[i].veze.dodaj(path)       #i dodajem njegove veze

            #novaGrana = Edge(path, i)             
            #self.grane.append(novaGrana)


    """def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None: # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e"""