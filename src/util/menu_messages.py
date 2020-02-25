def meni():
    '''
    Metoda za ispis mogucih opcija korisniku.
    :return:
    '''

    print("\n\nIzaberite opciju: ")
    print("\tOpcija broj 1 - Pretrazivanje teksta")
    print("\tOpcija broj 2 - Izlazak iz programa")

def check_correct_operation():
    operation = input("\nOpcija: ")
    while operation not in ["1", "2"]:
        print("\n\nUneli ste nepostojecu opciju!\nMolimo unesite ponovo.")
        operation = input("\nNovi unos: ")
    return operation

def input_path():
    return input("\n\nUneti putanju do foldera \n("
                 "Za folder u okviru projekta potrebno je uneti slovo P zatim ? i onda nazi foldera (P?python-2.7.7-docs-html)\n"
                 "a za apsolutnu putanju slovo A zatim ? i onda apsolutnu putanju (A?C:\\Users\...)\n"
                 "ako zelite default-nu putanju unesite D zatim ? (D?):")
