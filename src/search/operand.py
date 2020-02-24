def AND_operation(dictionary_1, dictionary_2):
    '''
    Funkcija vraca rezultat koji sadrzi prvu i drugu rec.
    :param dictionary_1:
    :param dictionary_2:
    :return:
    '''
    result = {}
    for key, value in dictionary_1.items():
        if key in dictionary_2.keys():
            result[key] = value + dictionary_2[key]
        else:
            continue
    return result

def OR_operation(dictionary_1, dictionary_2):
    '''
    Funkcija vraca razultat koji sadrzi ili prvu ili drugu rec.
    :param dictionary_1:
    :param dictionary_2:
    :return:
    '''
    result = {}
    for key, value in dictionary_1.items():
        result[key] = value
    for key, value in dictionary_2.items():
        if key not in result.keys():
            result[key] = value
        else:
            result[key] += value

    return result

def NOT_operation(dictionary_1, dictionary_2):
    '''
    Funkcija vraca rezultat koji sadrzi prvu rec, a ne sadrzi drugu rec.
    :param dictionary_1:
    :param dictionary_2:
    :return:
    '''
    result = {}
    for key, value in dictionary_1.items():
        if key not in dictionary_2.keys():
            result[key] = value
    return result

def use_operand(dictionary_first_word, dictionary_second_word, operand):
    if operand == 'AND':
        return AND_operation(dictionary_first_word, dictionary_second_word)
    elif operand == 'OR':
        return OR_operation(dictionary_first_word, dictionary_second_word)
    elif operand == 'NOT':
        return NOT_operation(dictionary_first_word, dictionary_second_word)
    else:
        return None


