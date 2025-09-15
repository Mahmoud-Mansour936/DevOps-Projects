from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "newsletter")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "root")

# Optional: log to console
app.logger.setLevel("DEBUG")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/', methods=['GET'])
def healthcheck():
    return "✅ Backend is running!"

@app.route('/signup', methods=['POST'])
def signup():
    try:
        # Support JSON and form data
        if request.is_json:
            email = request.json.get('email', '').strip()
        else:
            email = request.form.get('email', '').strip()

        if not email:
            app.logger.warning("No email provided.")
            return jsonify({"error": "Email is required"}), 400

        # Log the attempt
        app.logger.info(f"Received signup request for: {email}")

        # Connect and insert
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO subscribers (email) VALUES (%s)", (email,))
        conn.commit()
        cur.close()
        conn.close()

        app.logger.info(f"✅ Email {email} inserted into database.")

        return jsonify({"message": "Signed up successfully!"}), 200

    except mysql.connector.Error as db_err:
        app.logger.error(f"MySQL Error: {db_err}")
        return jsonify({"error": f"MySQL Error: {db_err}"}), 500
    except Exception as e:
        app.logger.error(f"Unexpected Error: {e}")
        return jsonify({"error": f"Unexpected Error: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
