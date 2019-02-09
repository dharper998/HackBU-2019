import requests
import json

def getArticles(input):
    articles = requests.get('http://159.203.144.49:3000/keywords?'
    'keyword=eq.' + input)
    JSONarticles = articles.json()
    return JSONarticles

def getPublications(articleData):
    publications = []
    for dict in articleData:
        publications.append(dict['publication_id'])


def main():
    i = input("Enter a health problem (ex: Cancer, Diabetes): ")
    articleData = getArticles(i)
    getPublications(articleData)
    #print(articleData)


main()
