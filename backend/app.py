from flask import Flask, jsonify
from flask_cors import CORS

import os
import psycopg2

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is working!"

@app.route("/health")
def health():
    return "OK"

@app.route('/api/message')
def get_message():
    return jsonify(message="Hello from backend!")

@app.route("/db-test")
def db_test():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS']
        )
        return "Connected to DB successfully!"
    except Exception as e:
        return f"DB connection failed: {str(e)}"


@app.route("/add-sample")
def add_sample():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS']
        )
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name TEXT);")
        cur.execute("INSERT INTO test_table (name) VALUES ('DockerUser') RETURNING id;")
        conn.commit()
        cur.close()
        return "Inserted into DB!"
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
