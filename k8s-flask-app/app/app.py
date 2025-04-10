from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

@app.route('/')
def home():
    return "Flask app is running with PostgreSQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)