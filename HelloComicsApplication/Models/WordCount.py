import string
import os

from HelloComicsApplication.Utilities.MakeLexicon import getLexicon

pronouns_file = 'pronouns.txt'
conjunctions_file = 'conjunctions.txt'

pronoun_lst = getLexicon(pronouns_file)
conjunction_lst = getLexicon(conjunctions_file)

class WordCount:

    def __init__(self):
        self.word_frequent = {}

    def update(self, text):

        # clean text
        for char in string.punctuation:
            text = text.replace(char, ' ')
        text = text.lower()

        word_list = text.split()

        # print pronoun_lst
        # print conjunction_lst

        # initail word-count dictionary
        # filter out pronouns and conjunctions
        for word in word_list:
            if word not in pronoun_lst and word not in conjunction_lst:
                # print word
                self.word_frequent[word] = self.word_frequent.get(word, 0) + 1


    def findTop5(self):

        # sort the word_frequent
        sorted_list = sorted(self.word_frequent.items(), key = lambda x:x[1], reverse = True)
        if len(sorted_list) <= 5:
            return sorted_list
        else:
            return sorted_list[:5]



if __name__ == '__main__':
    pass