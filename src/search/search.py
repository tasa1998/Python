import re

from src.search.operand import use_operand


def take_word(sentence):
    '''
    Funkcija nalazi rec koja u sebi sadrzi velika, mala slova i brojeva.
    :param word:
    :return:
    '''
    return re.findall('(?:[a-zA-Z0-9]+)', sentence)


def print_out(dictionary):
    '''
    Funkcija ispisuje fajl u kome se nalazi prosledjena reci broj ponavljanja prosledjene reci.
    :param dictionary:
    :return:
    '''
    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        print('Fajl: ', key, ', broj ponavljanja: ', dictionary[key], '\n')


def do_search(trie):
    '''
    Funkcija vrsi pretragu na osnovu unete reci ili vise reci koje su odvojene AND, OR ili NOT operatorom.
    :param trie:
    :return:
    '''
    wanted_words = input("\n\nUnesite rec koju zelite da pronadjete: ")
    list_of_words = take_word(wanted_words)

    if 'AND' in list_of_words or 'OR' in list_of_words or 'NOT' in list_of_words:
        if len(list_of_words) < 3:      #ako se nalazi AND, OR ili NOT lista unetih reci mora sadrzati 3 reci
            raise Exception
    if len(list_of_words) == 1 and list_of_words[0].isalnum():      #ako je unete 1 rec nadji je u recniku
        dictionary = trie.find_word(list_of_words[0].lower(), trie.root)
        print_out(dictionary)
    elif len(list_of_words) > 1:        #ako je duzina lista unetih reci veca od 1
        if 'AND' in list_of_words or 'OR' in list_of_words or 'NOT' in list_of_words:   #ako je uneto AND, OR ili NOT
            dictionary_first_word = trie.find_word(list_of_words[0].lower(), trie.root) #recnik 1 reci
            dictionary_second_word = trie.find_word(list_of_words[2].lower(), trie.root) #recnik 2 reci
            operand = list_of_words[1]                                                  #koji operand je unesen (and, or ili not)
        else:
            dictionary = {}
            for word in list_of_words:            #ako korisnik unese npr. python about posmatramo kao da je uneo python or about
                if len(dictionary) > 0:
                    temporary_dictionary = trie.find_word(word.lower(), trie.root)
                    dictionary = use_operand(dictionary, temporary_dictionary, 'OR')
                else:
                    dictionary = trie.find_word(word.lower(), trie.root)
            print_out(dictionary)
    print("\n\nUkupan broj fajlova u kojima je pronadjena trazena reci/reci je: " + str(len(dictionary.keys())))
