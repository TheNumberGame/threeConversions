from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/ftm")
def render_response():
    
    answer = float(request.args['ft']) * 0.3048
    
    return render_template('ftm.html', response = answer)
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
