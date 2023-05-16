from flask import Flask, render_template, request, flash, redirect, url_for

from db.dbTask import ListTaskDataBase
from model.Task import Task


app = Flask(__name__)
db = ListTaskDataBase


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
        state = 'Pendiente'

        task = Task(title=request.form["title"], description=request.form["description"],
                    responsible=request.form["responsible"], state=state)

        db.insertTask(task=task)
        # flash(' Tarea Registrada.', 'success')

    return redirect(url_for('home'))


@app.route("/all")
def all_task():
    db = ListTaskDataBase()
    tasks = db.getAllTask()
    return render_template("all_tasks.html", tasks=tasks)







# Change Task State to "En Proceso"
@app.route('/cambiar_proceso/<id>', methods=['POST'])
def cambiar_proceso():
    db = ListTaskDataBase()
    task_id = request.form['id']
    db.change_state_proceso(task_id)
    return render_template("all_tasks.html")



# Change Task State to "Finalizado"
@app.route('/cambiar_terminado/<id>', methods=['POST'])
def cambiar_terminado():
    db = ListTaskDataBase()
    task_id = request.form['id']
    db.change_state_finalizado(task_id)
    return render_template("all_tasks.html")





app.run(debug=True)
