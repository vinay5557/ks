'todo list controller'
import json
from flask import request

from flask import jsonify
from flask import current_app

# in memory todo list storage
todo_list = []

def list_items():
    'GET todo list'
    current_app.logger.info('todo controller called, func: list')
    return jsonify({
        'todoList': todo_list
    })

def add():
    'POST add item into todo list'
    current_app.logger.info('todo controller called, func: add')

    data = json.loads(request.data.decode("utf-8"))
    item = data['newItem']

    todo_list.append(item)

    return jsonify({
        'todoList': todo_list
    })

def delete():
    'POST delete item from list'
    current_app.logger.info('todo controller called, func: delete')

    data = json.loads(request.data.decode("utf-8"))
    item = data['item']

    if item in todo_list:
        todo_list.remove(item)

    return jsonify({
        'todoList': todo_list
    })
