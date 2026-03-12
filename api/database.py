# need 3 things here:
# 1. add a new score
# 2. get one persons score by name
# 3. get whoever has the highest score
# all hitting the same scores.db that the console app created

import sqlite3

DB_PATH = "../console/scores.db"


# Open a connection to the database.
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Save a new score to the database.
def add_score(first_name, second_name, score):
    conn = get_connection()
    conn.execute(
        "INSERT INTO scores (first_name, second_name, score) VALUES (?, ?, ?)",
        (first_name, second_name, score)
    )
    conn.commit()
    conn.close()


# Get the score for one person.
def get_score(first_name, second_name):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM scores WHERE first_name = ? AND second_name = ?",
        (first_name, second_name)
    ).fetchone()
    conn.close()
    return row


# Get all people with the highest score.
def get_top_scorers():
    conn = get_connection()
    top = conn.execute("SELECT MAX(score) FROM scores").fetchone()[0]
    rows = conn.execute(
        "SELECT * FROM scores WHERE score = ? ORDER BY first_name, second_name",
        (top,)
    ).fetchall()
    conn.close()
    return rows, top

