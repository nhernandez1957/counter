
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'visits' not in session:
        session ['visits'] = 1 
    else:
        session ['visits'] += 1
    return render_template("index.html", visits = session['visits'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return render_template("index.html")

if __name__=="__main__":  
    app.run(debug=True, port = 5001)  