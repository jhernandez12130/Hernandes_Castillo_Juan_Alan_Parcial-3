from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Error al obtener datos de la API'}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)