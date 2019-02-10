from flask import Flask, render_template, request
from h1 import doStuff
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_post():
    formInput = request.form['Medical']
    pubs = doStuff(formInput)
    pub1=pubs[0][0]
    pub2=pubs[1][0]
    pub3=pubs[2][0]
    pub4=pubs[3][0]
    pub5=pubs[4][0]
    return render_template("search.html", ab1=pub1['abstract'], title1=pub1['title'], ab2=pub2['abstract'], title2=pub2['title'], ab3=pub3['abstract'], title3=pub3['title'],
    ab4=pub4['abstract'], title4=pub4['title'], ab5=pub5['abstract'], title5=pub5['title'], input=formInput)

@app.route("/search.html")
def search():
    return render_template("search.html")

if __name__=="__main__":
    app.run(debug=True)
