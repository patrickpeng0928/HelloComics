import string

from HelloComicsApplication.Utilities.MakeLexicon import getLexicon

pronouns_file = 'pronouns.txt'
conjunctions_file = 'conjunctions.txt'

pronoun_lst = getLexicon(pronouns_file)
conjunction_lst = getLexicon(conjunctions_file)


class Comics:
    def __init__(self, comics = {}):
        self.comics = comics
        self.keyword_comics = {}

    def create_keywords(self):
        for comic, text in self.comics.iteritems():
            # clean text
            for char in string.punctuation:
                text = text.replace(char, ' ')
            text = text.lower()
            # remove duplicate words
            word_list = list(set(text.split()))

            for word in word_list:
                if word not in pronoun_lst and word not in conjunction_lst:
                    try:
                        self.keyword_comics[word].append(comic)
                    except KeyError:
                        self.keyword_comics[word] = [comic]

    def key_search(self, key):
        comic_list = self.keyword_comics.get(key, [])
        return comic_list


if __name__ == '__main__':
    d = {
        "Barrel - Part 1": "Don't we all.",
        "Petit Trees (sketch)": "'Petit' being a reference to Le Petit Prince, which I only thought about halfway through the sketch",
        "Island (sketch)": "Hello, island"
    }
    comics = Comics(d)
    comics.create_keywords()
    print comics.keyword_comics
