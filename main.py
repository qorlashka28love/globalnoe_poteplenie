from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/fquestion")
def page2():
    return render_template("fquestion.html")

@app.route("/squestion")
def page3():
    return render_template("squestion.html")
app.run(debug=True)
