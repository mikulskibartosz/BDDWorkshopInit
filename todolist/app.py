from flask import Flask, jsonify, request


app = Flask(__name__)

tasks = []
next_id = 0


@app.route('/tasks')
def get_tasks():
    global tasks
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def create_task():
    global tasks
    global next_id
    task = request.get_json()
    task['id'] = next_id
    next_id = next_id + 1
    tasks.append(task)
    return '', 201


@app.route('/tasks/completed/<int:id>', methods=['PUT'])
def complete_task(id):
    global tasks
    to_remove = list(filter(lambda x: x['id'] == id, tasks))
    for removed in to_remove:
        tasks.remove(removed)
    return '', 202
