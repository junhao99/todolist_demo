import json

from flask import app, Flask, render_template, jsonify, request

from todo.db import TodoDB

print(__name__)
app = Flask(__name__)


@app.route('/')
def hello():
    db = TodoDB()

    todo = db.read_all()

    return render_template('index.html', todo_list=todo)


@app.route('/todo/<int:todo_id>', methods=["DELETE"])
def delete(todo_id):
    db = TodoDB()
    todo = db.delete(todo_id)
    result = db.read_id(todo_id)
    db.close()

    # print(result)
    # if not result:
    #     return "false"
    # t = {"id":result[0],"content":result[1]}
    return jsonify({'existed': True}) if result else \
        jsonify({'existed': False})






@app.route('/add', methods=["POST"])
def add():
    data = request.get_json()
    print(data)
    print("ssssssssssss")
    db = TodoDB()
    db.create(data['text'])
    db.close()
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
