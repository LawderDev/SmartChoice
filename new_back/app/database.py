import sqlite3
import os
from flask import g

class DB(object):
    DATABASE = os.path.join(os.getcwd(), 'app', 'db', 'database.sqlite') # Path to your SQLite database file

    @staticmethod
    def get_db():
        """Get a database connection."""
        if 'db' not in g:
            print(DB.DATABASE)
            g.db = sqlite3.connect(DB.DATABASE)
            g.db.row_factory = sqlite3.Row  # Allows access to columns by name
        return g.db

    @staticmethod
    def close_db(e=None):
        """Close the database connection."""
        db = g.pop('db', None)
        if db is not None:
            db.close()

    @staticmethod
    def insert(query, data):
        """Insert data into the database."""
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query, data)
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def find_one(query, data):
        """Find one record in the database."""
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query, data)
        return cursor.fetchone()

    @staticmethod
    def find(query, data=()):
        """Find multiple records in the database."""
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query, data)
        return cursor.fetchall()

    @staticmethod
    def remove(query, data):
        """Remove records from the database."""
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query, data)
        db.commit()

    @staticmethod
    def update(query, data):
        """Update records in the database."""
        db = DB.get_db()
        cursor = db.cursor()
        cursor.execute(query, data)
        db.commit()