from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('openhouse-ai.db')

@app.route('/')
def hello_world():
    try:
        data = request.json
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ")
        return 'Hello, World!'
    except KeyError:
        return json.dumps({"error", {"message": "keyerror"}})
