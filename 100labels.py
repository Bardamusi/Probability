"""
Story:
Aliens come to earth to build a intergalactic super highway, and our planet is in the way.
It will be destroyed to make space. However since the aliens are generous they will give us a chance.
They invite the 100 smartest minds to come and pass their test.
There will be a 100 pictures of objects in a room, and each human will get a card with a word.
Each picture has a word on the back with it's meaning in the alien language.
In english we could have a picture with :) , with on the back the word smiley.

One by one the humans will go into the room, where they are not allowed to change anything.
Each can make 50 guesses. They need to match their word to the correct object.
A guess is made by picking picture and flipping it to see the word on the back written down.

Humanity only wins if all 100 humans match their word to the correct object.
And earth won't be destroyed. They are allowed to devise a strategy but as the game starts
, no communication or cheating is allowed

The aliens were sure that this test is just a formality given that the chance to guess
correctly for each human is 0.5, which suggests that for all 100 to guess correctly the chances are
0.5^100 which is infinitesimally small, however a far better solution exists. Can you find it ?
"""

import random


def correct_guess(picture, word, meaning):
    """
    :param picture: The picture picked by a human
    :param word: The word that has been given to this human,
                which needs to match what is in the picture
    :param meaning: a dictionary with the true mapping of picture to word
    :return: True if guess is correct, the **real** meaning if guess is incorrect
    """

    if meaning[picture] == word:  # This would be a correct guess
        return True
    else:
        return meaning[picture]


def create_proper_strategy(n_objects, word_list, picture_list):
    """
    :param word_list: of words
    :param picture_list: of labels of pictures
    :return: dictionary linking a word to a picture,
    the strategy here is that if a human has word that word is randomly associated with a picture.
    if it's correct he is done, if it's wrong he takes the word he found and looks at the picture associated with
    that word
    """
    association = picture_list[:]
    random.shuffle(association)

    strategy = {}
    for i in range(0, n_objects):
        key = word_list[i]
        strategy[key] = association[i]

    return strategy


def correct_picture_to_word(n_objects, picture_list, word_list):
    """
    :param n_objects: number of pictures and words
    :param picture_list: list with labels for pictures
    :param word_list: list with labels for words
    :return: dictionary mapping the correct picture to the correct word
    Slightly confusing since pictures are named 0-99, and words are "named" 0-99
    """

    association = word_list[:]
    random.shuffle(association)  # We randomly assign the meaning of each word to

    meaning = {}
    for picture in range(0, n_objects):
        key = picture_list[picture]
        meaning[key] = association[picture]  # Each picture has an a meaning

    return meaning


def give_each_human_word(human_list, word_list):
    """
    :param human_list: list of labels for humans
    :param word_list: list of labels for words
    :return: dictionary mapping each word to a person.
    So if we had the words boat, car, plane and we would have 3 people A, B, C
    We could link A -> boat, B -> plane C -> car
    """
    association = word_list[:]
    random.shuffle(association)
    mapping = {}
    for i in range(len(human_list)):
        key = human_list[i]
        mapping[key] = association[i]  # We associate each human with an word

    return mapping


def initialise_game(n_objects):
    """
    :param n_objects: int, number of people/words/pictures we assume to be the same
    :return: 3 dictionaries, first - all human-word pairs, second, correct picture - word pairs,
        third human-strategy
    """

    human_list = list(range(0, n_objects))  # We call the people 0 to 99 as their name
    word_list = list(range(n_objects, 2 * n_objects))  # We label the words from 100 to 199
    picture_list = list(range(2 * n_objects, 3 * n_objects))  # There are a hundred pictures we label them from 200 to 299

    human_word_pairs = give_each_human_word(human_list, word_list)
    picture_word = correct_picture_to_word(n_objects, picture_list, word_list)
    strategy_pairs = create_proper_strategy(n_objects, word_list, picture_list)

    return human_word_pairs, picture_word, strategy_pairs

def play_game(n_objects, n_guesses):



if __name__ == "__main__":

    n_objects = 100
    n_guesses = 50

    print(initialise_game(10))

