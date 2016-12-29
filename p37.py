from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

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

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bs0bj = BeautifulSoup(html,"html.parser")
    internalLinks = getInternalLinks(bs0bj,splitAddress(siteUrl)[0])
    externalLinks = getExternallinks(bs0bj,splitAddress(siteUrl)[0])

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是："+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")





