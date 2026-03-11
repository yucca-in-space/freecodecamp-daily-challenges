'''
Given a string of words, return a new string where each word is replaced by its length.

    Words in the given string will be separated by a single space
    Keep the spaces in the returned string.

For example, given "hello world", return "5 5".

'''


def convert_words(string):

    words_list = string.split()

    new_string=""

    for word in words_list:
        new_string += str(len(word)) + " "

    new_string = new_string.rstrip()

    return new_string
