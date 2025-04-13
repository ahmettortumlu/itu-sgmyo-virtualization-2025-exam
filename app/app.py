# app.py
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS security_logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            source_ip VARCHAR(15),
            destination_ip VARCHAR(15),
            protocol VARCHAR(10),
            port INTEGER,
            event_type VARCHAR(50),
            severity VARCHAR(10),
            description TEXT
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        database=os.getenv('DB_NAME', 'mydb'),
        user=os.getenv('DB_USER', 'myuser'),
        password=os.getenv('DB_PASSWORD', 'mypassword')
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM security_logs ORDER BY timestamp DESC;')
    logs = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(logs)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
