from flask import Flask, render_template, request
from h1 import doStuff
import webscraping
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_post():
    formInput = request.form['Medical']
    pubs = doStuff(formInput)
    if(len(pubs)<5):
        return render_template("index.html")
    pub1=pubs[0][0]
    pub2=pubs[1][0]
    pub3=pubs[2][0]
    pub4=pubs[3][0]
    pub5=pubs[4][0]
    title1=pub1['title']
    title2=pub2['title']
    title3=pub3['title']
    title4=pub4['title']
    title5=pub5['title']
    url1=webscraping.search(title1)
    url2=webscraping.search(title2)
    url3=webscraping.search(title3)
    url4=webscraping.search(title4)
    url5=webscraping.search(title5)
    wiki = webscraping.webscrape(formInput)

    return render_template("search.html", ab1=pub1['abstract'], title1=title1, url1=url1, ab2=pub2['abstract'], title2=title2, url2=url2, ab3=pub3['abstract'], title3=title3, url3=url3,
    ab4=pub4['abstract'], title4=title4, url4=url4, ab5=pub5['abstract'], title5=title5, url5=url5, input=formInput, wiki=wiki)

@app.route("/search.html")
def search():
    return render_template("search.html")

if __name__=="__main__":
    app.run(debug=True)
