from flask import Flask, render_template
from db.dbTask import ListTaskDataBase

app = Flask(__name__)
db = ListTaskDataBase

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new")
def new_task():
    return render_template("task.html")

@app.route("/all")
def all_task():
    tasks= db.getAllTask()
    return render_template("all_tasks.html", tasks= tasks)

app.run(debug=True)
