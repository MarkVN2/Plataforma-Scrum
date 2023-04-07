from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/exp") #ONLY FOR TESTING REMOVE LATER
def navbar():
    return render_template('navbar.html') #

@app.route("/head")
def header():
    return render_template('example_page.html')