from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/add_hospital')
def add_doctor():
    return render_template("add hospital.html")

@app.route('/add_doctor')
def add_hospital():
    return render_template("add doctor.html")

app.run(host='0.0.0.0', port=8080)