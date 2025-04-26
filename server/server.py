from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Store the latest data
latest_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    global latest_data
    data = request.json
    latest_data = data
    return jsonify({"status": "success"})

@app.route('/api/latest')
def get_latest():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)