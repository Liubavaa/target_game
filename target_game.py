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
            if letter in word and len(word) > 4:
                word_list.append(word[:-1])
        dictionary.close()
    for word in word_list:
        for char in word:
            if char not in letters:
                idx = word_list.index(word)
                word_list[idx] = 0
                break
    for word in word_list:
        if word != 0:
            word_tuple_list = []
            for char in word:
                if (char, word.count(char)) not in word_tuple_list:
                    word_tuple_list.append((char, word.count(char)))
            for char_amount in word_tuple_list:
                if char_amount[1] > letters.count(char_amount[0]):
                    idx = word_list.index(word)
                    word_list[idx] = 0
                    break
    word_list = [i for i in word_list if i]
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
    for word in user_words:
        if word in words_from_dict or letter not in word or len(word) < 4:
            idx = user_words.index(word)
            user_words[idx] = 0
        else:
            for char in word:
                if char not in letters:
                    idx = user_words.index(word)
                    user_words[idx] = 0
                    break
    for word in user_words:
        if word != 0:
            word_tuple_list = []
            for char in word:
                if (char, word.count(char)) not in word_tuple_list:
                    word_tuple_list.append((char, word.count(char)))
            for char_amount in word_tuple_list:
                if char_amount[1] > letters.count(char_amount[0]):
                    idx = user_words.index(word)
                    user_words[idx] = 0
                    break
    user_pure_words = [i for i in user_words if i]
    return user_pure_words


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
    words_from_dict = get_words('en.txt', letters)
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
