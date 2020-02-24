from src.util.file_util import load_file_and_build_structure
from src.util.menu_messages import input_path, meni, check_correct_operation
from src.search.search import do_search

if __name__ == '__main__':
    print("-------------PRETRAZIVANJE TEKSTA-------------")
    while True:
        try:
            path = input_path()
            if path.__contains__('P?') or path.__contains__('A?') or path.__contains__('D?'):
                within_project = path.split('?')[0]
                path_project = path.split('?')[1]
                trie = load_file_and_build_structure(within_project, path_project)
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