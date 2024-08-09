# task_manager.py

tasks = []

def add_task(task):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "text": task, "completed": False})

def remove_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

def mark_task_completed(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True

def get_tasks():
    return tasks
