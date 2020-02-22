

class Edge:
    def __init__(self, izlazni, ulazni):
        self._pocetak = izlazni
        self._kraj = ulazni
    def endpoints(self):
        return (self._pocetak, self._kraj)

    def __hash__(self): # will allow edge to be a map/set key
        return hash( (self._pocetak, self._kraj) )
    def __str__(self):
        return '({0},{1},{2})'.format(self._pocetak,self._kraj)