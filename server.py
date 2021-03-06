from flask import Flask, request, jsonify, app
import json
import sqlite3

app = Flask(__name__)

DATABASE_NAME = 'openhouse-ai.db'


def setup_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS logs ('
        'userId varchar(9) NOT NULL, '
        'sessionId varchar(9) NOT NULL, '
        'time datetime NOT NULL, '
        'type varchar NOT NULL, '
        'properties varchar NOT NULL'
        ')'
    )
    cursor.close()
    connection.commit()
    connection.close()


@app.route('/add-log', methods=['POST'])
def add_log():
    try:
        data = json.loads(request.json)
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        for action in data['actions']:
            cursor.execute(
                "INSERT INTO logs (userId, sessionId, time, type, properties) VALUES (?, ?, ?, ?, ?)",
                (data['userId'], data['sessionId'], action['time'], action['type'], json.dumps(action['properties']))
            )
        cursor.close()
        connection.commit()
        connection.close()

        return jsonify({'message': 'added log to database'}), 200
    except (KeyError, TypeError) as e:
        app.logger.error(e)
        return jsonify({"message": "error: please pass a json request in the format specified in the documentation."}), 400


@app.route('/get-logs', methods=['GET'])
def get_logs():
    try:
        data = request.data

        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM logs WHERE userId=? AND time<=? AND time>=? and type=?",
            (data['userId'], data['startTime'], data['endTime'], data['type'])
        )
        rows = cursor.fetchall()
        output = jsonify(rows)
        cursor.close()
        connection.close()

        return output
    except (KeyError, TypeError) as e:
        app.logger.error(e)
        return jsonify({"message": "error: please pass a request in the format specified in the documentation."}), 400


setup_database()
