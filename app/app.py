from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
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
    cur.execute('SELECT * FROM items;')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)