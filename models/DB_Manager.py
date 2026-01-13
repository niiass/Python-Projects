"""
DBManager is class to help with managing data in SQLite database

__init__:
It is used to create DBManager type object with specific .db file path
create_table() is called inside this method

create_table:
It is used to create RealEstate table according to RealEstate class attributes
Uses Exception Handling and Context Manager

insert_data:
It gets list of RealEstate child classes objects and inserts them into table using their to_database() method
through list comprehension
Uses Exception Handling and Context Manager
"""

import sqlite3

class DBManager:
    def __init__(self, db_name="Project/data/RealEstate.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        comm = """
            CREATE TABLE IF NOT EXISTS RealEstate (
                SerialNumber integer NOT NULL,
                ListYear integer NOT NULL,
                DateRecorded datetime NOT NULL,
                Town text NOT NULL,
                Address text NOT NULL,
                AssessedValue float NOT NULL,
                SaleAmount float NOT NULL,
                SalesRatio float NOT NULL,
                ResidentialType text NOT NULL
                )
        """

        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute(comm)
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")

    def insert_data(self, data):
        data_to_insert = [row.to_database() for row in data]
        query = "INSERT INTO RealEstate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.executemany(query, data_to_insert)
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")