#!/usr/bin/env python
# Exercise 1
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesnt matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Notes:
#   - There are three examples below. In this case, store_to_dict_read is
#     generally faster. See the associated .ipynb.
###############################################################################


def store_to_dict_readlines():
    with open('words.txt') as f:
        words = f.readlines()
    d = {word.strip(): 0 for word in words}
    return d


def store_to_dict_readsplit():
    with open('words.txt') as f:
        words = f.read().split()
    d = {word: 0 for word in words}
    return d


def store_to_dict_readsplitlines():
    with open('words.txt') as f:
        words = f.read().splitlines()
    d = {word: 0 for word in words}
    return d


def store_to_dict_for():
    with open('words.txt') as f:
        d = {word.strip(): 0 for word in f}
    return d

##############################################################################


def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict_for()
    if "this" in words_dict:
        print "Yup."
    if "qwertyuiop" in words_dict:
        print "Hmm."

if __name__ == '__main__':
    main()
