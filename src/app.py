from flask import Flask, render_template, request

app = Flask(__name__)

# Normal routes
@app.route("/")
def index():
    return render_template('pt/home.html', home=True)

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


#!ENG ROUTES

# Normal routes 
@app.route("/en")
def index_en():
    return render_template('home_en.html', home=True)

@app.route("/en/metodologia/introducao")
def metInt_en():
    return render_template('en/metodologia/met_int.html')

@app.route("/en/metodologia/oqueescrum")
def metOqs_en():
    return render_template('en/metodologia/met_oqs.html')

@app.route("/en/metodologia/visao")
def metVis_en():
    return render_template('en/metodologia/met_vis.html')

@app.route("/en/metodologia/pilares")
def metPil_en():
    return render_template('en/metodologia/met_pil.html')

@app.route("/en/metodologia/autoavaliacao")
def metAuto_en():
    return render_template('en/metodologia/met_auto.html')

@app.route("/en/metodologia/team")
def metTeam_en():
    return render_template('en/metodologia/met_team.html')

# Product owner routes
@app.route('/en/product-owner/introducao')
def poInt_en():
    return render_template('en/product_owner/po_int.html')

@app.route('/en/product-owner/backlog')
def poBac_en():
    return render_template('en/product_owner/po_back.html')

# Scrum master routes
@app.route('/en/scrum-master/introducao')
def smInt_en():
    return render_template('en/scrum_master/sm_int.html')

@app.route('/en/scrum-master/burndown')
def smBrn_en():
    return render_template('en/scrum_master/sm_burn.html')

# Development team routes
@app.route("/en/development-team")
def devTeam_en():
    return render_template('en/dev_team/dev-team.html')

# Other routes
@app.route("/en/conclusao")
def conclusion_en():
    return render_template('en/outros/conclusion.html')

@app.route('/en/materiais')
def materials_en():
    return render_template('en/outros/mat.html', buttons=False)

@app.route('/en/glossario')
def glossary_en():
    return render_template('en/outros/glossario.html', buttons=False)

@app.route('/en/tutorial')
def tutorial_en():
    return render_template('en/outros/tutorial.html', buttons=False)

@app.route('/en/form')
def avaliation_en():
    return render_template('en/outros/forms.html', buttons=False,form=True)

if __name__=='__main__': #MAKES THE SERVER START UPON RUNNING THE CODE.
    app.run(debug=True, use_debugger=True,use_reloader=True, host="0.0.0.0")