from typing import List


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    pass


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt', ['e', 'm', 'x', 'p', 'w', 'z', 'w', 'p', 'i'])
    []
    """
    letter = letters[4]
    word_list = []
    with open(f, "r") as dictionary:
        for word in dictionary:
            if letter in word and len(word) > 3:
                word_list.append(word[:-1])
    for word in word_list:
        for char in word:
            if char not in letters:
                idx = word_list.index(word)
                word_list[idx] = 0
                break
    word_list = [i for i in word_list if i]
    print(word_list)


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
