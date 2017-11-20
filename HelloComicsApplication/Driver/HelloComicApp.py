
from HelloComicsApplication.DataIngestion.ComicData import getLastNum, getAltText, getComicNum, getComicName

########## GLOBAL VARIALBES ##########
from HelloComicsApplication.Models import WordCount, ComicSearch

LATEST_COMIC = 'https://xkcd.com/info.0.json'
URL_PREFIX = 'https://xkcd.com/'
URL_POSTFIX = '/info.0.json'

######################################

# get the last number of comics
n = getLastNum()

### create a dictionary to keep comic and its alt text
comics = {}

for i in range(1, n + 1):
    comic_url = URL_PREFIX + str(i) + URL_POSTFIX
    comic_name = getComicName(comic_url)
    alt_text = getAltText(comic_url)
    # print getComicNum(comic_url)
    # print comic_name
    # print alt_text
    if comic_name in comics:
        print 'duplicate comic names found!'
        comic_name = comic_name + '1'
    comics[comic_name] = alt_text

### Found 5 most commonly used word  used as alt-text for the comics on XKCD
wc = WordCount.WordCount()

for key, value in comics.iteritems():
    wc.update(value)

top5 = [key for key, _ in wc.findTop5()]

print '1. Here are the 5 most commonly used words used as alt-text for the comics on XKCD:'
print '{}'.format(', '.join(top5))


### keyword search

print 'Please input a keyword to search comics on XKCD:'
keyword = raw_input()

cs = ComicSearch.Comics(comics)
cs.create_keywords()

#### find the comics contain the keyword
keyword = keyword.lower()
comic_list = cs.key_search(keyword)

#### find top 5 word in each comic
results = {}

if comic_list:
    for comic in comic_list:
        comic_wc = WordCount.WordCount()
        comic_wc.update(comics[comic])
        results[comic] = [key for key, _ in comic_wc.findTop5()]
    print 'Here is the list of comics that contains keyword: {}, and the 5 most commonly used words of those related comics:'.format(keyword)
    for key, value in results.iteritems():
        print '{}: {}'.format(key, ', '.join(value))
else:
    print 'There is no comic contains keyword:', keyword

