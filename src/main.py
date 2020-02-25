from src.util.file_util import load_file_and_build_structure
from src.util.menu_messages import input_path, meni, check_correct_operation
from src.search.search import do_search
from src.structure.graph2 import Graph
from src.text.parser import Parser
import os
from src.structure.set import Set

"""brojevi = Set()
brojevi.dodaj(1)
brojevi.dodaj(2)
brojevi1 = Set()
brojevi1.dodaj(2)
brojevi1.dodaj(4)

brojevi.presek(brojevi1)
resenje = Set()
resenje = brojevi.presek(brojevi1)
resenje.ispisi()"""

if __name__ == '__main__':
    print("-------------PRETRAZIVANJE TEKSTA-------------")
    while True:
        try:
            path = input_path()
            if path.__contains__('P?') or path.__contains__('A?') or path.__contains__('D?'):
                within_project = path.split('?')[0]
                if len(path.split('?')[1] )>1:
                    path_project = path.split('?')[1]
                else:
                    path_project = 'python-2.7.7-docs-html'
                trie, graf = load_file_and_build_structure(within_project, path_project)
                break
            else:
                raise Exception
        except:
            print("Unesite unos ponovo! \n")
            pass
    print("-------------FUNKCIONALNOSTI-------------")
    meni()
    operation = check_correct_operation()
    while operation != '2':
        if operation == "1":
            try:
                do_search(trie)
            except:
                print("Unos nije validan!")
                pass
            meni()
        operation = check_correct_operation()
    print("Dovidjenja! :)")