from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/exp") #ONLY FOR TESTING REMOVE LATER
def navbar():
    return render_template('conclusao.html') #

@app.route("/head")
def header():
    return render_template('example_page.html')
    
@app.route("/nav")
def nav():
    return render_template('navbar.html')

if __name__=='__main__': #MAKES THE SERVER START UPON RUNNING THE CODE.
    app.run(debug=True, use_debugger=True,use_reloader=True)