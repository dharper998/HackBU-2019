from flask import Flask, render_template
from h1 import main
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=['POST'])
def search():
    input = request.form['Medical']
    h1.main(input)
    return render_template("search.html")

if __name__=="__main__":
    app.run(debug=True)
