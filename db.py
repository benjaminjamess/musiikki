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