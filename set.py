import copy
class Set:
    def __init__(self):
        self.reci = {}

    def dodaj(self, link):
        if link not in self.reci:
            self.reci[link] = link

    def obrisi(self, link):
        del (self.reci[link])

    def ispisi(self):
        for i in self.reci:
            print(i)

    def unija(self, skup):
        unijaa=copy.copy(self)
        for i in skup.reci:
            if i not in self.reci:
                unijaa.dodaj(i)
        return unijaa

    def presek(self, skup):
        presekk = Set()
        for i in self.reci:
            if i in skup.reci:
                presekk.dodaj(i)
        return presekk

    def komplement(self, skup):
        komplementt = copy.copy(self)
        for i in skup.reci:
            if i in self.reci:
                komplementt.obrisi(i)
        return komplementt