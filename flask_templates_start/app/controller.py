from app import app
from app.models.task import *
from flask import render_template, request
from app.models.todo_list import add_new_task, tasks


@app.route("/")
def index():
    return render_template("index.html", title="Home", tasks=tasks)


@app.route("/add-task", methods=["POST"])
def add_task():
    task_title = request.form["title"]
    task_description = request.form["description"]
    new_task = Task(task_title, task_description, False)
    add_new_task(new_task)
    print(request.form)
    return render_template("index.html", title="Home", tasks=tasks)
