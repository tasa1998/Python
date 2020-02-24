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
        if len(list_of_words) < 3:
            raise Exception
    if len(list_of_words) == 1 and list_of_words[0].isalnum():
        dictionary = trie.find_word(list_of_words[0].lower(), trie.root)
        print_out(dictionary)
    elif len(list_of_words) > 1:
        if 'AND' in list_of_words or 'OR' in list_of_words or 'NOT' in list_of_words:
            dictionary_first_word = trie.find_word(list_of_words[0].lower(), trie.root)
            dictionary_second_word = trie.find_word(list_of_words[2].lower(), trie.root)
            operand = list_of_words[1]
        else:
            dictionary_words = {}
            for word in list_of_words:
                if len(dictionary_words) > 0:
                    temporary_dictionary = trie.find_word(word.lower(), trie.root)
                    dictionary_words = use_operand(dictionary_words, temporary_dictionary, 'OR')
                else:
                    dictionary_words = trie.find_word(word.lower(), trie.root)
            print_out(dictionary_words)
