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

  def add_product(self, product, amount):
    cursor = self.conn.cursor()
    cursor.execute(
      "INSERT INTO inventory (product, amount) VALUES (?, ?)", (product, amount)
    )
    self.conn.commit()

  def remove_product(self, product, amount):
    cursor = self.conn.cursor()
    cursor.execute(
      "SELECT amount FROM inventory WHERE product=?", (product,)
    )
    result = cursor.fetchone()
    if result:
      currentInventory = result[0]
      if currentInventory >= amount:
        cursor.execute("UPDATE inventory SET amount=? WHERE product=?",
        (currentInventory - amount, product))
        self.conn.commit()
      else:
        print(f"Insufficient amount of {product} in stock.")
    else:
      print(f"{product} not found in stock.")
        