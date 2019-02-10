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
    return publications

def fetchPubs(publicationData):
    finalPublications = []
    for publication in publicationData:
        #print(publication)
        finalPub = requests.get('http://159.203.144.49:3000/publications?'
        'id=eq.' + publication)
        finalPublications.append(finalPub.json())
    return finalPublications

def main():
    i = input("Enter a health problem (ex: Cancer, Diabetes): ")
    articleData = getArticles(i)
    publicationData = getPublications(articleData)
    finalPublications = fetchPubs(publicationData)
    print(finalPublications)
main()
