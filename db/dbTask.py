import psycopg2

from model import Task


class ListTaskDataBase:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", database="lisTask", user="postgres",
                                           port="5432",
                                           password="lucas3030")
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
    def deleteTask(self):
        pass

    # UpdateTask
    def updateTask(self):
        pass
