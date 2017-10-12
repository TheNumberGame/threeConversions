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
def render_Ftml():
    return render_template('Ltml.html')
    
@app.route("/response")
def render_response():
    if 'ft' in request.args[]:
        answer = float(request.args['ft']) * 0.3048
        return render_template('response.html', response = answer)
    elif 'eh' in request.args[]:
        answer = (float(request.args['eh'])*9.81)/3.711
        return render_template('response.html', response = answer)
    else 'lr' in request.args[]:
        answer = float(request.args['lr'])*1000
        return render_template('response.html', response = answer)
    
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
