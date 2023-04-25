from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new")
def new_task():
    return render_template("task.html")

@app.route("/all")
def all_task():
    return render_template("all_tasks.html")

app.run(debug=True)
