from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bs0bj = BeautifulSoup(html,"html.parser")
for link in bs0bj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
