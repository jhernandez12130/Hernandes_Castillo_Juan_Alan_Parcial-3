

from flask import Flask, jsonify

app = Flask(__name__)
tasks = [
    {"id": 1, "nombre": "John", "enable": True},
    {"id": 2, "nombre": "Jessie", "enable": False},
    {"id": 3, "nombre": "Johanna", "enable": True},
    {"id": 4, "nombre": "braulio", "enable": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)