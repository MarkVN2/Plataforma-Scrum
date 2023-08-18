from flask import Flask, render_template, request

app = Flask(__name__)

# Normal routes
@app.route("/")
def index():
    return render_template('home.html', home=True)

@app.route("/metodologia/introducao")
def metInt():
    return render_template('pt/metodologia/met_int.html')

@app.route("/metodologia/oqueescrum")
def metOqs():
    return render_template('pt/metodologia/met_oqs.html')

@app.route("/metodologia/visao")
def metVis():
    return render_template('pt/metodologia/met_vis.html')

@app.route("/metodologia/pilares")
def metPil():
    return render_template('pt/metodologia/met_pil.html')

@app.route("/metodologia/autoavaliacao")
def metAuto():
    return render_template('pt/metodologia/met_auto.html')

@app.route("/metodologia/team")
def metTeam():
    return render_template('pt/metodologia/met_team.html')

# Product owner routes
@app.route('/product-owner/introducao')
def poInt():
    return render_template('pt/product_owner/po_int.html')

@app.route('/product-owner/backlog')
def poBac():
    return render_template('pt/product_owner/po_back.html')

# Scrum master routes
@app.route('/scrum-master/introducao')
def smInt():
    return render_template('pt/scrum_master/sm_int.html')

@app.route('/scrum-master/burndown')
def smBrn():
    return render_template('pt/scrum_master/sm_burn.html')

# Development team routes
@app.route("/development-team")
def devTeam():
    return render_template('pt/dev_team/dev-team.html')

# Other routes
@app.route("/conclusao")
def conclusion():
    return render_template('pt/outros/conclusion.html')

@app.route('/materiais')
def materials():
    return render_template('pt/outros/mat.html', buttons=False)

@app.route('/glossario')
def glossary():
    return render_template('pt/outros/glossario.html', buttons=False)

@app.route('/tutorial')
def tutorial():
    return render_template('pt/outros/tutorial.html', buttons=False)

@app.route('/form')
def avaliation():
    return render_template('pt/outros/forms.html', buttons=False,form=True)

if __name__=='__main__': #MAKES THE SERVER START UPON RUNNING THE CODE.
    app.run(debug=True, use_debugger=True,use_reloader=True, host="0.0.0.0")