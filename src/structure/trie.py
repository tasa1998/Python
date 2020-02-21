class TrieNode():
    def __init__(self, char, parent):
        self.char = char
        self.parent = parent
        self.children = []
        self.path_number_of_repetitions = {}

    def add_to_children(self):
        if self.parent:
            self.parent.children.append(self)


class Trie(object):
    def __init__(self):
        self.root = TrieNode(" ", None)

    def add_word(self, new_word, node, path, char_index=0):
        '''
                Funkcija koja dodaje rec u strukturu
                :param new_word:
                :param node:
                :param path:
                :param char_index:
                :return:
        '''

        if char_index < len(new_word):
            char = new_word[char_index]
            char_exists = False
            node_child = None
            for node_child in node.lista_dece:
                if node_child.char == char:
                    char_exists = True
                    break
            if not char_exists:
                new_node = TrieNode(char, node)
                new_node.add_to_children()
                self.add_word(new_word, new_node, path, char_index + 1)
                return None
            else:
                self.add_word(new_word, node_child, path, char_index + 1)
                return None
        else:
            if path not in node.path_number_of_repetitions:
                node.path_number_of_repetitions[path] = 1
            else:
                node.path_number_of_repetitions[path] = node.path_number_of_repetitions[path] + 1
            return None

    def find_word(self, wanted_word, node, char_index=0):
        '''
        Funkcija pronalazi trazenu rec u strukturi.
        :param wanted_word:
        :param node:
        :param char_index:
        :return:
        '''

        if char_index < len(wanted_word):
            char = wanted_word[char_index]
            for child in node.children:
                if char == child.char:
                    return self.find_word(wanted_word, child, char_index + 1)

        if char_index == len(wanted_word):
            return node.path_number_of_repetitions
        else:
            return None