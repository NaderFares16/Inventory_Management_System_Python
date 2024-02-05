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

  def consult_product(self, product):
    cursor = self.conn.cursor()
    cursor.execute(
      "SELECT amount FROM inventory WHERE product=?", (product,))
    result = cursor.fetchone()
    if result:
      return result[0]
    else:
      return 0
    
  def list_products(self):
    cursor = self.conn.cursor()
    cursor.execute(
      "SELECT product FROM inventory"
    )
    products = cursor.fetchall()
    return [product[0] for product in products]
  
System = Management("inventory.db")

# ADD PRODUCT IN DATABASE (PRODUCT / AMOUNT)

System.add_product("T-Shirt", 20)
System.add_product("Pants", 30)
System.add_product("Shoes", 15)

# CONSULT THE AMOUNT OF PRODUCT

shirt_stock = System.consult_product("T-Shirt")
print(f"Amount of T-Shirts in Stock: {shirt_stock}")

# REMOVE PRODUCT AMOUNT IN DATABASE

System.remove_product("Pants", 20)

# LIST PRODUCTS IN DATABASE

products_stock = System.list_products()
print(f"Products in Stock: {products_stock}")
