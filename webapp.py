from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/ftm")
def render_ftm():
    return render_template('ftm.html')

@app.route("/etm")
def render_etm():
    return render_template('etm.html')

@app.route("/Ltml")
def render_Ltml():
    return render_template('Ltml.html')
    
@app.route("/response")
def render_response():
    if 'ft' in request.args:
        answer = float(request.args['ft']) * 0.3048     
    elif 'eh' in request.args:
        answer = (float(request.args['eh'])*9.81)/3.711
    elif 'lr' in request.args:
        answer = String(float(request.args['lr'])*1000)+'mL'
        
    return render_template('response.html', response = answer)
       
