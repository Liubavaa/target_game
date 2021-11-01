"""
for God's sake, lets finish it
"""
from typing import List
import random
import string
import sys


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = [[], [], []]
    for i in range(3):
        for _ in range(3):
            grid[i].append(random.choice(string.ascii_uppercase))
    return grid


def get_words(path: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt', ['e', 'm', 'x', 'p', 'w', 'z', 'w', 'p', 'i'])
    ['wime', 'wipe']
    """
    letter = letters[4]
    word_list = []
    with open(path, "r", encoding='UTF-8') as dictionary:
        for word in dictionary:
            word = word[:-1].lower()
            if letter in word and len(word) > 3:
                if all(char in letters for char in word):
                    word_tuple_list = []
                    for char in word:
                        if (char, word.count(char)) not in word_tuple_list:
                            word_tuple_list.append((char, word.count(char)))
                    if all(char_a_amount[1] <= letters.count(char_a_amount[0])
                           for char_a_amount in word_tuple_list):
                        word_list.append(word)
    return word_list


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    for line in sys.stdin:
        user_words += [line]
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['wipe', 'miw', 'wim', 'mipp', 'xemw'],\
    ['e', 'm', 'x', 'p', 'w', 'z', 'w', 'p', 'i'], ['wime', 'wipe'])
    ['xemw']
    """
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


def results():
    """
    Return amount of correct words, dictionary words, non written correct words, pure words
    """
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
