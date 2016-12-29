from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
#获取页面所有内链列表
def getInternalLinks(bs0bj,includeUrl):
    internallinks = []
    #找出所有以"/"开头的链接
    for link in bs0bj.findAll("a",href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                internallinks.append(link.attrs['href'])
    return internallinks

#获取页面所有外链的列表
def getExternallinks(bs0bj,excludeUrl):
    externallinks = []
    #找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bs0bj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs0bj = BeautifulSoup(html,"html.parser")
    externalLinks = getExternallinks(bs0bj,splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getExternallinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")



