from typing import List
import random
import urllib.request
import re
import string
import sys


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    >>> generate_grid()
    o
    """
    alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', 'є', 'і', 'ї', 'ґ']
    grid = []
    while len(grid) < 5:
        chr = random.choice(alph)
        if chr not in grid:
            grid.append(chr)
    return grid


def get_words(path: str, letters: List[str]):
    """
    Reads the file and checks the words with rules and returns a list of words and their part of language.
    >>> get_words('https://raw.githubusercontent.com/brown-uk/dict_uk/master/data/dict/base.lst',\
                    ['й', 'й', 'й', 'й', 'й'])
    [('йняти', 'verb'), ('йог', 'noun'), ('йога', 'noun'), ('йод', 'noun'), ('йодат', 'noun'), ('йодид', 'noun'),\
 ('йодил', 'noun'), ('йодит', 'noun'), ('йодль', 'noun'), ('йола', 'noun'), ('йолоп', 'noun'), ('йомен', 'noun'),\
 ('йон', 'noun'), ('йорж', 'noun'), ('йорж', 'noun'), ('йорк', 'noun'), ('йот', 'noun'), ('йота', 'noun'),\
 ('йти', 'verb'), ('йтися', 'verb')]
    """
    result = []
    with urllib.request.urlopen(path) as total_txt:
        whole_list = re.findall(r"\n\w+ /n|\n\w+ /v|\n\w+ /adj|\n\w+ adv|\n\w+ n|\n\w+ v|\n\w+ adj|\n\w+ noun",
                                total_txt.read().decode('utf8'))
        for line in whole_list:
            word = line.split()[0]
            if len(word) < 6:
                if line[1] in letters:
                    if 'n' in line:
                        result.append((word, 'noun'))
                    elif 'adv' in line:
                        result.append((word, 'adverb'))
                    elif 'v' in line:
                        result.append((word, 'verb'))
                    elif 'adj' in line:
                        result.append((word, 'adjective'))
    return result


def get_pure_user_words(user_words: List[str], letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['wipe', 'miw', 'wim', 'mipp', 'xemw'],\
    ['e', 'm', 'x', 'p', 'w', 'z', 'w', 'p', 'i'], ['wime', 'wipe'])
    ['xemw']

    letter = letters[4]
    pure_words = []
    for word in user_words:
        if letter in word and len(word) > 3:
            if all(char in letters for char in word):
                word_tuple_list = []
                for char in word:
                    if (char, word.count(char)) not in word_tuple_list:
                        word_tuple_list.append((char, word.count(char)))
                if all(char_a_amount[1] <= letters.count(char_a_amount[0])
                       for char_a_amount in word_tuple_list):
                    if word not in words_from_dict:
                        pure_words.append(word)
    return pure_words
    """
    pass


def results():
    """
    Return amount of correct words, dictionary words, non written correct words, pure words

    letters = []
    for char_3 in generate_grid():
        for char in char_3:
            letters.append(str(char).lower())

    result = 0
    user_words = get_user_words()
    words_from_dict = get_words('en', letters)
    for word in user_words:
        if word in words_from_dict:
            result += 1

    non_written_words = []
    for word in words_from_dict:
        if word not in user_words:
            non_written_words.append(word)

    pure_words = get_pure_user_words(user_words, letters, words_from_dict)

    with open('result.txt', 'w', encoding='UTF-8') as result_file:
        result_file.writelines(result)
        result_file.writelines(words_from_dict)
        result_file.writelines(non_written_words)
        result_file.writelines(pure_words)
    result_file.close()

    return result, words_from_dict, non_written_words, pure_words
    """
    pass
