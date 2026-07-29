import sqlite3


DATABASE_PATH = "agencyos.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raw_request TEXT NOT NULL,
            service TEXT,
            summary TEXT,
            priority TEXT,
            questions TEXT,
            created_at TEXT
        )
        """
    )

    connection.commit()
    connection.close()