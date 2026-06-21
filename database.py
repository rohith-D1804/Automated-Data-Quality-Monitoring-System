import sqlite3


def get_connection():
    return sqlite3.connect("data_quality.db")


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_results (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        scan_time TEXT,

        quality_score REAL,

        quality_status TEXT,

        missing_count INTEGER,

        duplicate_count INTEGER,

        outlier_count INTEGER,

        schema_issue_count INTEGER
    )
    """)

    conn.commit()

    conn.close()




from datetime import datetime

def save_scan_result(
    quality_score,
    quality_status,
    validation_results
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scan_results (

        scan_time,
        quality_score,
        quality_status,
        missing_count,
        duplicate_count,
        outlier_count,
        schema_issue_count

    )

    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,

    (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        quality_score,

        quality_status,

        validation_results["missing_values"]["issue_count"],

        validation_results["duplicates"]["issue_count"],

        validation_results["outliers"]["issue_count"],

        validation_results["schema"]["issue_count"]
    ))

    conn.commit()

    conn.close()



def show_results():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM scan_results"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


from database import show_results
show_results()