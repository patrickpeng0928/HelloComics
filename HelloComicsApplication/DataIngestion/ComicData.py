import requests
import json

LATEST_COMIC = 'https://xkcd.com/info.0.json'
URL_PREFIX = 'https://xkcd.com/'
URL_POSTFIX = '/info.0.json'

def readULR(url):
    response =requests.get(url)
    try:
        dic = json.loads(response.content)
    except ValueError as e:
        print 'cannot find JSON object from url: {}'.format(url)
        dic = {}
    finally:
        return dic

def getLastNum():
    last_comic = readULR(LATEST_COMIC)
    return last_comic['num']

def getAltText(url):
    comic = readULR(url)
    if comic:
        alt_text = comic['alt'].encode('utf-8')
    else:
        alt_text = ""
    return alt_text

def getComicName(url):
    comic = readULR(url)
    if comic:
        comic_name = comic['title'].encode('utf-8')
    else:
        comic_name = ""
    return comic_name

def getComicNum(url):
    comic = readULR(url)
    if comic:
        comic_num = comic['num']
    else:
        comic_num = int(url.split('/')[-2])
    return comic_num

if __name__ == '__main__':
    n = getLastNum()
    print n
    comic_url = URL_PREFIX + str(403) + URL_POSTFIX
    print comic_url
    dic = readULR(comic_url)
    print dic['alt']
    alt_text = getAltText(comic_url)
    print alt_text
    print getComicName(comic_url)
    print getComicNum(comic_url)