import sqlite3

class Management:
  def __init__(self, database):
    self.conn = sqlite3.connect(database)
    self.create_inventory_database()

  def create_inventory_database(self):
    cursor = self.conn.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY,
        product TEXT,
        amount INTEGER 
      )
    ''')
    self.conn.commit()