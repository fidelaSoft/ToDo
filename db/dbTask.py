import psycopg2
from model import Task


class ListTaskDataBase:
    def __init__(self):
        self.connection = psycopg2.connect(host="ep-polished-band-986724.us-east-2.aws.neon.tech", database="ToDo",
                                           user="Lucas-30c", password="ZToIlGPNE7v5")
        self.cursor = self.connection.cursor()

    # All TASK
    def getAllTask(self):
        self.cursor.execute("SELECT * FROM task ORDER BY id")
        task = self.cursor.fetchall()
        return task

    # Insert TASK
    def insertTask(self, task: Task):
        SQLinsert = f"insert into task(title, description, responsible, state) values ('{task.title}','{task.description}','{task.responsible}','{task.state}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()

    # Delete Task
    def deleteTask(self, id):
        self.cursor.execute("DELETE FROM task WHERE id = {0} ".format(id))
        self.connection.commit()

    # UpdateTask
    def updateTask(self, task: Task):
        q = f"UPDATE task SET title = '{task.title}', description = '{task.description}', responsible = '{task.responsible}', state = '{task.state}' WHERE id = {task.id}"
        self.cursor.execute(q)
        self.connection.commit()











    # Change Task State to "En Proceso"
    def change_state_proceso(self, id):
        SQLupdate = f"UPDATE task SET state = 'En Proceso' WHERE id = {id}"
        self.cursor.execute(SQLupdate)
        self.connection.commit()

    # Change Task State to "Finalizado"
    def change_state_finalizado(self, id):
        SQLupdate = f"UPDATE task SET state = 'Finalizado' WHERE id = {id}"
        self.cursor.execute(SQLupdate)
        self.connection.commit()







    # Close DB
    def closeDB(self):
        self.connection.close()
