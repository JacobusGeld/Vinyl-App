import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form.get("search")
        result = f"You searched for: {user_input}"

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO searches (query) VALUES (%s)",
            (user_input,)
        )

        conn.commit()
        cur.close()
        conn.close()

    return render_template("index.html", result=result)