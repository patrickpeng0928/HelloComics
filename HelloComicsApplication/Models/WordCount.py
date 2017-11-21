import string
import os

from HelloComicsApplication.Utilities.MakeLexicon import getLexicon

pronouns_file = 'pronouns.txt'
conjunctions_file = 'conjunctions.txt'

### create two lexicons of pronoun and conjunction to filter out words
pronoun_lst = getLexicon(pronouns_file)
conjunction_lst = getLexicon(conjunctions_file)

class WordCount:

    def __init__(self):
        self.word_frequent = {}

    def update(self, text):
        '''
        word count on text
        :param text: input text
        :return: dictionary, key: word, value: total occurance of the key in the text
        '''
        # clean text
        # remove punctuations
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
                # update dictionary
                self.word_frequent[word] = self.word_frequent.get(word, 0) + 1


    def findTop5(self):
        '''
        find 5 most commonly used word in the word count dictionary
        :return: list of string, at most 5 words
        '''
        # sort the word_frequent
        sorted_list = sorted(self.word_frequent.items(), key = lambda x:x[1], reverse = True)
        # if words number is no greater than 5
        if len(sorted_list) <= 5:
            return sorted_list
        else: # words number is greater than 5, return first 5 words
            return sorted_list[:5]


#### test
if __name__ == '__main__':
    pass