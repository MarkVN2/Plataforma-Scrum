from flask import Flask, render_template

app = Flask(__name__)

# Normal routes
@app.route("/")
def index():
    return render_template('home.html')

# pages about 'metodologia' 

@app.route("/metodologia/introducao")
def metInt():
    return render_template('')

@app.route("/metodologia/oqueescrum")
def metOqe():
    return render_template('')

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

@app.route('/product-owner/valordoproduto')
def poVal():
    return render_template('')

@app.route('/product-owner/backlog')
def poBac():
    return render_template('')

# pages about 'scrum master'

@app.route('/scrum-master/introducao')
def smInt():
    return render_template('sm_int.html')

@app.route('/scrum-master/burndown')
def smBrn():
    return render_template('')

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
    return render_template('')

@app.route('/glossario')
def glossary():
    return render_template('')

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