import sqlite3

DB_PATH = "scores.db"


# Save all rows from the CSV into the scores table.
def save_rows(rows):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            second_name TEXT,
            score INTEGER
        )
    """)
    for row in rows:
        conn.execute(
            "INSERT INTO scores (first_name, second_name, score) VALUES (?, ?, ?)",
            (row["First Name"], row["Second Name"], int(row["Score"]))
        )
    conn.commit()
    conn.close()

