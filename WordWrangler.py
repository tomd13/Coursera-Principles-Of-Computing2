"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    temp_list = []
    for item in list1:
        if item not in temp_list:
            temp_list.append(item)
    return temp_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    temp_list = []
    for item in list1:
        if item in list2:
            temp_list.append(item)
    for item in list2:
        if item in list1:
            temp_list.append(item)

    return remove_duplicates(temp_list)


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    dummy_list1 = list1[:]
    dummy_list2 = list2[:]
    merged_list = []
    while dummy_list1 != [] and dummy_list2 != []:
        if dummy_list1[0] < dummy_list2[0]:
            merged_list.append(dummy_list1.pop(0))
        else:
            merged_list.append(dummy_list2.pop(0))
    if dummy_list1 == []:
        for item in dummy_list2:
            merged_list.append(item)
    if dummy_list2 == []:
        for item in dummy_list1:
            merged_list.append(item)
    return merged_list


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1

    list_split1 = list1[:len(list1) / 2]
    list_split2 = list1[len(list1) / 2:]

    return merge(merge_sort(list_split1), merge_sort(list_split2))


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    new_strings = []
    for item in rest_strings:
        for idx in range(len(item) + 1):
            new_strings.append(item[:idx] + first + item[idx:])
    return rest_strings + new_strings


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    words_file = netfile.readlines()
    words = [word[:-2] for word in words_file]

    return words


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
