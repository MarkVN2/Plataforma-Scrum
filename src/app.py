from flask import Flask, render_template, request

app = Flask(__name__)

# Normal routes
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/metodologia/introducao")
def metInt():
    return render_template('met_int.html')

@app.route("/metodologia/oqueescrum")
def metOqs():
    return render_template('met_oqs.html')

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

# pages about 'product owner'

@app.route('/product-owner/introducao')
def poInt():
    return render_template('po_int.html')

@app.route('/product-owner/backlog')
def poBac():
    return render_template('po_back.html')

# pages about 'scrum master'

@app.route('/scrum-master/introducao')
def smInt():
    return render_template('sm_int.html')

@app.route('/scrum-master/burndown')
def smBrn():
    return render_template('sm_burn.html')

# pages about  'devteam'

@app.route("/development-team")
def devTeam():
    return render_template('dev-team.html')

# others

@app.route("/conclusao")
def conclusion():
    return render_template('conclusion.html')

@app.route('/materiais')
def materials():
    return render_template('mat.html')

@app.route('/glossario')
def glossary():
    return render_template('glossario.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

# Tests
@app.route("/pag", methods =["GET", "POST"]) #ONLY FOR TESTING REMOVE LATER
def pag():
    return render_template('test.html') #

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
    app.run(debug=True, use_debugger=True,use_reloader=True, host="0.0.0.0")