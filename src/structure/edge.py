

class Edge:
    def __init__(self, izlazni, ulazni):
        self.pocetak = izlazni                  #polazni cvor
        self.kraj = ulazni                      #cvor na koji pokazuje
    def endpoints(self):
        return (self.pocetak, self.kraj)        #vraca cvorove

    def __hash__(self): # will allow edge to be a map/set key
        return hash((self.pocetak, self.kraj))
    def __str__(self):
        return '({0},{1},{2})'.format(self.pocetak,self.kraj)
