import requests
import json

LATEST_COMIC = 'https://xkcd.com/info.0.json'
URL_PREFIX = 'https://xkcd.com/'
URL_POSTFIX = '/info.0.json'

class RetrieveComicData:
    def __init__(self):
        self.comic = {}

    def readUrl(self, url):
        response =requests.get(url)
        dic = {}
        try:
            dic = json.loads(response.content)
        except ValueError as e:
            print 'cannot find JSON object from url: {}'.format(url)
            dic['num'] = int(url.split('/')[-2])
        finally:
            return dic

    def getJSONDictFromUrl(self, url):
        self.comic = self.readUrl(url)

    def getLastNum(self, url):
        last_comic = self.readUrl(url)
        return last_comic['num']

    def getAltText(self):
        if self.comic:
            alt_text = self.comic['alt'].encode('utf-8')
        else:
            alt_text = ""
        return alt_text

    def getComicName(self):
        if self.comic:
            comic_name = self.comic['title'].encode('utf-8')
        else:
            comic_name = ""
        return comic_name

    def getComicNum(self):
        if self.comic:
            comic_num = self.comic['num']
        else:
            comic_num = self.comic['num']
        return comic_num

if __name__ == '__main__':
    comic_data = RetrieveComicData()
    n = comic_data.getLastNum(LATEST_COMIC)
    print n
    comic_url = URL_PREFIX + str(403) + URL_POSTFIX
    print comic_url
    comic_data.getJSONDictFromUrl(comic_url)
    print comic_data.comic
    print comic_data.comic['alt']
    alt_text = comic_data.getAltText()
    print alt_text
    print comic_data.getComicName()
    print comic_data.getComicNum()