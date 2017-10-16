from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

def getLinks(url):
    result = []
    html = urlopen('https://en.wikipedia.org'+url)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id':'bodyContent'}).findAll('a',href=re.compile('(^/wiki/)((?!:).)*$'))

def main():
    random.seed(datetime.datetime.now())
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) > 0:
        new = links[random.randint(0, len(links)-1)].attrs['href']
        print(new)
        links = getLinks(new)

if __name__ == '__main__':
    main()
