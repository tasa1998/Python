from os import listdir
from os.path import join, isdir, splitext, abspath, split
from time import time

from src.structure.graph2 import Graph
from src.structure.trie import Trie
from src.text.parser import Parser

list_operand = ['AND', 'OR', 'NOT']


def read_the_file_paths(root_directory_path, list_of_paths):
    '''
    Funkcija cita putanje fajlova i dodaje html fajlove u listu putanja.
    :param root_directory_path:
    :param list_of_paths:
    :return:
    '''
    for directory in listdir(root_directory_path):
        path = join(root_directory_path, directory)

        if isdir(path):                    #ako se u folderu nalazi folder
            read_the_file_paths(path, list_of_paths)

        file_extension = splitext(path)[1]
        if file_extension == '.html':       #ako je fajl html dodaj njegovu putanju u listu
            list_of_paths.append(path)
    return list_of_paths


def load_file_and_build_structure(within_project, path_project):
    '''
    Ucitavanje svih html fajlova i popunjavanje strukture.
    :param within_project:
    :param path_project:
    :return:
    '''
    root_directory_path = ''
    if within_project == 'P' or within_project == 'D':
        model_path_main = abspath(__file__)
        root_directory_path = split(model_path_main)[0][:-8] + path_project
    elif within_project == 'A':
        root_directory_path = path_project

    parser = Parser()
    trie = Trie()
    paths = []
    graf = Graph()
    time1 = time()

    try:
        path_file = read_the_file_paths(root_directory_path, paths)
    except:
        print('Doslo je do greske prilikom inicijalizacije!')
        raise Exception

    for path in path_file:
        links, words = parser.parse(path)
        graf.insert_vertex(links, words, path)
        for word in words:
            trie.add_word(word.lower(), trie.root, path)

    time2 = time()
    print("Vreme ucitavanja podataka iz fajla i kreiranja strukture je: "+ str(time2-time1))
    print()
    return trie,graf
