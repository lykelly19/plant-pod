from flask import (render_template)

from flask import Flask
app = Flask(__name__, template_folder='./templates')

@app.route('/')
def hello_world():
    x = "Fiona"
    return render_template("index.html", x=x)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/story')
def story_page():
    return render_template("ourStory.html")
