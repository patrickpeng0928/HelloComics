import requests
import json

LATEST_COMIC = 'https://xkcd.com/info.0.json'
URL_PREFIX = 'https://xkcd.com/'
URL_POSTFIX = '/info.0.json'

class RetrieveComicData:
    '''
    retrieve json content from XKCD url
    1. get last comic number
    2. get json content of a specific comic(with comic number)
    '''

    def __init__(self):
        self.comic = {}

    def readUrl(self, url):
        '''
        get JSON content from XKCD API
        :param url: https://xkcd.com/{{comic_num}}/info.0.json
        :return: json to dictionary, at least get comic number in dictionary
        '''
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
        '''
        update class attribute
        :param url: url for XKCD API
        :return: N/A
        '''
        self.comic = self.readUrl(url)

    def getLastNum(self, url):
        '''
        get the number of the latest comic
        :param url: LATEST_COMIC = 'https://xkcd.com/info.0.json'
        :return: int
        '''
        last_comic = self.readUrl(url)
        return last_comic['num']

    def getAltText(self):
        '''
        get alt text of the comic
        :return: string
        '''
        # chekc 'alt' in self.comic dictionary
        if 'alt' in self.comic:
            alt_text = self.comic['alt'].encode('utf-8')
        else: # not get from url
            alt_text = ""
        return alt_text

    def getComicName(self):
        '''
        get comic name
        :return: string
        '''
        # check 'title in self.comic dictionary
        if 'title' in self.comic:
            comic_name = self.comic['title'].encode('utf-8')
        else: # not get from url
            comic_name = ""
        return comic_name

    def getComicNum(self):
        '''
        get comic number
        :return: int
        '''
        # all comic dictionaries contain 'num'
        comic_num = self.comic['num']
        return comic_num

#### test
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