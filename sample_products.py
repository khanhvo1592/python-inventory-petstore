import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create products table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        aisle TEXT NOT NULL,
        bay INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Sample data for 20 products with manual IDs
sample_products = [
    # Dog Food
    (1001, "Royal Canin Mini Adult", "Dog Food", 25.99, 50, "A", 1),
    (1002, "Pedigree Puppy Growth", "Dog Food", 15.99, 30, "A", 2),
    (1003, "Purina Pro Plan", "Dog Food", 35.99, 40, "A", 3),
    
    # Cat Food
    (2001, "Whiskas Adult", "Cat Food", 12.99, 45, "B", 1),
    (2002, "Royal Canin Kitten", "Cat Food", 28.99, 35, "B", 2),
    (2003, "Friskies Indoor", "Cat Food", 18.99, 40, "B", 3),
    
    # Toys
    (3001, "Dog Rubber Ball", "Toys", 8.99, 60, "C", 1),
    (3002, "Cat Fishing Rod", "Toys", 6.99, 50, "C", 2),
    (3003, "Chew Bone", "Toys", 12.99, 45, "C", 3),
    
    # Accessories
    (4001, "Leather Collar", "Accessories", 15.99, 30, "D", 1),
    (4002, "Dog Leash", "Accessories", 12.99, 40, "D", 2),
    (4003, "Stainless Bowl", "Accessories", 9.99, 50, "D", 3),
    
    # Grooming
    (5001, "Dog Shampoo", "Grooming", 14.99, 35, "E", 1),
    (5002, "Grooming Brush", "Grooming", 7.99, 40, "E", 2),
    (5003, "Toothbrush", "Grooming", 5.99, 45, "E", 3),
    
    # Medicine
    (6001, "Dewormer", "Medicine", 19.99, 25, "F", 1),
    (6002, "Flea Treatment", "Medicine", 22.99, 30, "F", 2),
    (6003, "Multivitamin", "Medicine", 29.99, 20, "F", 3),
    
    # Bedding
    (7001, "Plastic Dog Crate", "Bedding", 45.99, 15, "A", 4),
    (7002, "Cat Bed", "Bedding", 35.99, 20, "B", 4)
]

# Insert data into table
cursor.executemany('''
    INSERT INTO products (id, name, category, price, quantity, aisle, bay)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', sample_products)

# Save changes and close connection
conn.commit()
conn.close()

print("Successfully added 20 sample products to the database!")