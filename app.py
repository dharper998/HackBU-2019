from flask import Flask, render_template
from h1 import main
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_post():
    input = request.form['Medical']
    h1.main(input)

@app.route("/search.html")
def search():
    return render_template("search.html")

if __name__=="__main__":
    app.run(debug=True)
