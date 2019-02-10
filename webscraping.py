from bs4 import BeautifulSoup
import requests
import re
import subprocess


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


def search(input):
    subprocess.call("python3 scholar.py -c 1 --phrase \""+input+'\" >search.txt', shell=True)
    with open("search.txt", "r") as file:
        title = file.readline()
        url = file.readline()
        url = url.strip()
        url = url[4:]
    return url

def main():
    search("Paraneoplastic bleeding disorder due to isolated hypofibrinogenemia: a case report.")
main()
