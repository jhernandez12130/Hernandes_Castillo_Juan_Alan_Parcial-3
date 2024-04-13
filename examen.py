from flask import Flask, jsonify

app = Flask(__name__)

# Datos ficticios de la máquina
machine_info = {
    "hostname": "my-machine",
    "ip_address": "192.168.1.100"
}

@app.route('/machine-info', methods=['GET'])
def get_machine_info():
    return jsonify(machine_info)

if __name__ == '__main__':
    app.run(debug=True)
