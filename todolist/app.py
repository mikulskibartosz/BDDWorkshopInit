from flask import Flask, jsonify, request


app = Flask(__name__)

tasks = []


@app.route('/tasks')
def get_tasks():
    global tasks
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def create_task():
    global tasks
    task = request.get_json()
    task_id = len(tasks)
    task['id'] = task_id
    tasks.append(task)
    return '', 201


@app.route('/tasks/completed/<int:id>', methods=['PUT'])
def complete_task(id):
    global tasks
    to_remove = list(filter(lambda x: x['id'] == id, tasks))
    for removed in to_remove:
        tasks.remove(removed)
    return '', 202
