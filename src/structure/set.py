import copy
class Set:
    def __init__(self):
        self.reci = {}                      #set se sastoji od recnika

    def dodaj(self, link):                  #dodavanje reci u recnik
        if link not in self.reci:
            self.reci[link] = link

    def obrisi(self, link):                 #brisanje reci iz recnika
        del (self.reci[link])

    def ispisi(self):                       #ispis reci iz recnika
        for i in self.reci:
            print(i)

    def unija(self, skup):                     #uzimam recnik koji je napravljen u konstruktoru i uporedjujem sa recnikom sa kojim radim uniju, ako se u novom recniku nalaze neke reci koje u mom recniku ne postoje dodajem ih
        unijaa=copy.copy(self)
        for i in skup.reci:
            if i not in self.reci:
                unijaa.dodaj(i)
        return unijaa

    def presek(self, skup):                 #uzimam recnik koji vec imam i recnik sa kojim zelim da uradim presek, ako postoje reci koje se poklapaju dodajem ih u presek
        presekk = Set()
        for i in self.reci:
            if i in skup.reci:
                presekk.dodaj(i)
        return presekk

    def komplement(self, skup):             #uzimam recnik koji vec imam i drugi racnik sa kojim radim komplement, ako se rec nalazi u mom recniku i u drugom recniku brisem ih
        komplementt = copy.copy(self)
        for i in skup.reci:
            if i in self.reci:
                komplementt.obrisi(i)
        return komplementt