import sqlite3
import os

class Contacts:
    def __init__(self):
        self.db_name = ""

    def set_database_name(self, db_file):
        self.db_name = db_file
        if not os.path.exists(db_file):
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE contacts (
                        contact_id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE phones (
                        phone_id INTEGER PRIMARY KEY,
                        contact_id INTEGER,
                        phone_type TEXT NOT NULL,
                        phone_number TEXT NOT NULL,
                        FOREIGN KEY(contact_id) REFERENCES contacts(contact_id)
                    )
                ''')
                conn.commit()

    def get_database_name(self):
        return self.db_name

    def add_contact(self, first_name, last_name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO contacts (first_name, last_name) 
                VALUES (?, ?)
            ''', (first_name, last_name))
            conn.commit()

    def modify_contact(self, contact_id, first_name, last_name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE contacts 
                SET first_name = ?, last_name = ? 
                WHERE contact_id = ?
            ''', (first_name, last_name, contact_id))
            conn.commit()

    def add_phone(self, contact_id, phone_type, phone_number):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO phones (contact_id, phone_type, phone_number) 
                VALUES (?, ?, ?)
            ''', (contact_id, phone_type, phone_number))
            conn.commit()

    def modify_phone(self, phone_id, phone_type, phone_number):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE phones 
                SET phone_type = ?, phone_number = ? 
                WHERE phone_id = ?
            ''', (phone_type, phone_number, phone_id))
            conn.commit()

    def get_contact_phone_list(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT contacts.*, phones.* 
                FROM contacts 
                LEFT JOIN phones 
                ON contacts.contact_id = phones.contact_id
            ''')
            return cursor.fetchall()
