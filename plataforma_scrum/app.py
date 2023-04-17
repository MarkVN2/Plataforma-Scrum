from flask import Flask, render_template

app = Flask(__name__)

# Normal routes
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/metodologia/visao")
def metVis():
    return render_template('met_vis.html')

@app.route("/metodologia/pilares")
def metPil():
    return render_template('met_pil.html')

@app.route("/metodologia/autoavaliacao")
def metAuto():
    return render_template('met_auto.html')

@app.route("/metodologia/team")
def metTeam():
    return render_template('met_team.html')

@app.route("/development-team")
def devTeam():
    return render_template('dev-team.html')

# Tests
@app.route("/pag") #ONLY FOR TESTING REMOVE LATER
def pag():
    return render_template('conclusion.html') #

@app.route("/head")
def header():
    return render_template('header.html')
    
@app.route("/nav")
def nav():
    return render_template('navbar.html')

@app.route("/example")
def example():
    return render_template('example_page.html')

if __name__=='__main__': #MAKES THE SERVER START UPON RUNNING THE CODE.
    app.run(debug=True, use_debugger=True,use_reloader=True)