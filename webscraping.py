from bs4 import BeautifulSoup
import requests
import re


def webscrape(input):
    webpage = requests.get("http://en.wikipedia.org/wiki/" + input)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    p1 = soup.find_all('p')[1].get_text()
    p2 = soup.find_all('p')[2].get_text()
    paragraph = p1 + p2
    for i in range(30):
        remove = '\['+str(i)+'\]'
        paragraph = re.sub(remove, '', paragraph)
    return paragraph
