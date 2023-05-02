from flask import Flask, render_template, request, flash, redirect, url_for

from db.dbTask import ListTaskDataBase
from model.Task import Task

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new")
def new_task():
    return render_template("task.html")


# -----------  Insert new Task -----------
@app.route('/new/insertTask', methods=['POST'])
def saveInsertTask():
    db = ListTaskDataBase()
    if request.method == 'POST':
        state = 'En Proceso'

        task = Task(title=request.form.get("title"), description=request.form.get("description"),
                    responsible=request.form.get("responsible"), state=state)

        db.insertTask(task=task)
        # flash(' Tarea Registrada.', 'success')

    return redirect(url_for('home'))


@app.route("/all")
def all_task():
    return render_template("all_tasks.html")


app.run(debug=True)
