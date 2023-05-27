from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'Ammar'
    return render_template('index.html',name = name)

@app.route('/about')
def hello_ammar():
    return render_template('about.html')
app.run(debug = True)