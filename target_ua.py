"""
part of game to guess words that start with one of five letter
and is in corresponding part of language
"""
from typing import List
import random
import urllib.request
import re


def generate_grid() -> List[List[str]]:
    """
    Generates list of 5 letters - i.e. grid for the game.
    e.g. ['п', 'о', 'м', 'и', 'т']
    """
    alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
           'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', 'є', 'і', 'ї', 'ґ']
    grid = []
    while len(grid) < 5:
        char = random.choice(alp)
        if char not in grid:
            grid.append(char)
    return grid


def get_words(path: str, letters: List[str]):
    """
    Reads the file and checks the words with rules
    and returns a list of words and their part of language.
    >>> get_words('https://raw.githubusercontent.com/brown-uk/dict_uk/master/data/dict/base.lst',\
                    ['й', 'й', 'й', 'й', 'й'])
    [('йняти', 'verb'), ('йог', 'noun'), ('йога', 'noun'), ('йод', 'noun'), ('йодат', 'noun'),\
 ('йодид', 'noun'), ('йодил', 'noun'), ('йодит', 'noun'), ('йодль', 'noun'), ('йола', 'noun'),\
 ('йолоп', 'noun'), ('йомен', 'noun'), ('йон', 'noun'), ('йорж', 'noun'), ('йорж', 'noun'),\
 ('йорк', 'noun'), ('йот', 'noun'), ('йота', 'noun'), ('йти', 'verb'), ('йтися', 'verb')]
    """
    result = []
    with urllib.request.urlopen(path) as total_txt:
        whole_list = re.findall(
            r'\n\w+ /n|\n\w+ /v|\n\w+ /adj|\n\w+ adv|\n\w+ n|\n\w+ v|\n\w+ adj|\n\w+ noun',
            total_txt.read().decode('utf8')
        )
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


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    returns list of right user's words and missed right words
    >>> check_user_words(['йти', 'йог', 'йога', 'гора'], 'verb', ['й', 'й', 'й', 'й', 'й'],\
    [('йняти', 'verb'), ('йог', 'noun'), ('йога', 'noun'),('йод', 'noun'),\
    ('йодат', 'noun'), ('йодид', 'noun'),('йодил', 'noun'), ('йодит', 'noun'),\
    ('йодль', 'noun'), ('йола', 'noun'), ('йолоп', 'noun'), ('йомен', 'noun'),\
    ('йон', 'noun'), ('йорж', 'noun'), ('йорж', 'noun'), ('йорк', 'noun'), ('йот', 'noun'),\
    ('йота', 'noun'), ('йти', 'verb'), ('йтися', 'verb')])
    (['йти'], ['йняти', 'йтися'])
    """
    letters += 's'   # рядок просто, щоб використати летерс і не збільшувати кількість перевірок
    right_words = []
    miss_words = []
    for word_part in dict_of_words:
        if word_part[1] == language_part:
            if word_part[0] in user_words:
                right_words.append(word_part[0])
            else:
                miss_words.append(word_part[0])
    return right_words, miss_words
