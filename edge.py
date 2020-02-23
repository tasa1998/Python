

class Edge:
    def __init__(self, izlazni, ulazni):
        self.pocetak = izlazni
        self.kraj = ulazni
    def endpoints(self):
        return (self.pocetak, self.kraj)

    def __hash__(self): # will allow edge to be a map/set key
        return hash( (self.pocetak, self.kraj) )
    def __str__(self):
        return '({0},{1},{2})'.format(self.pocetak,self.kraj)
