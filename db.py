import sqlite3
from pathlib import Path
from flask import g


def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def initialize():
    schema_path = Path(__file__).with_name("schema.sql")
    con = get_connection()
    try:
        con.executescript(schema_path.read_text(encoding="utf-8"))
        item_columns = {row["name"] for row in con.execute("PRAGMA table_info(items)")}
        if "user_id" not in item_columns:
            con.execute("ALTER TABLE items ADD COLUMN user_id INTEGER REFERENCES users(id)")
            con.commit()

        item_foreign_keys = list(con.execute("PRAGMA foreign_key_list(items)"))
        if any(row["from"] == "rating" for row in item_foreign_keys):
            con.execute("PRAGMA foreign_keys = OFF")
            try:
                con.execute("BEGIN")
                con.execute("""
                    CREATE TABLE items_rebuilt (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        artist TEXT,
                        rating INTEGER,
                        user_id INTEGER REFERENCES users(id)
                    )
                """)
                con.execute("""
                    INSERT INTO items_rebuilt (id, title, artist, rating, user_id)
                    SELECT id, title, artist, rating, user_id FROM items
                """)
                con.execute("DROP TABLE items")
                con.execute("ALTER TABLE items_rebuilt RENAME TO items")
                con.commit()
            except Exception:
                con.rollback()
                raise
            finally:
                con.execute("PRAGMA foreign_keys = ON")
    finally:
        con.close()

def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    return g.last_insert_id    
    
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result