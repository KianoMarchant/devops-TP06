import os
import sys
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "DevOps TP06 API"})


@app.route('/health')
def health():
    return jsonify({"status": "healthy"})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
