from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "API is working!"

@app.route("/health")
def health():
    return "OK"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
