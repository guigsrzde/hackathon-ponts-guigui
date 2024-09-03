from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/prompt", methods = ['POST'])
def prompt():
    if request.method == 'POST':
        msg = request.form['prompt'].swapcase()
        return {"answer":msg}