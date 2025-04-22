import sqlite3
from datetime import datetime
from .category_manager import CategoryManager

class Inventory:
    def __init__(self):
        """Khởi tạo kết nối database"""
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()
        self.category_manager = CategoryManager()
        self.product_cache = {}
        
        # Tạo bảng products nếu chưa tồn tại
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                aisle TEXT NOT NULL,
                bay INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
        
        # List để lưu trữ lịch sử thay đổi
        self.change_history = []

    def add_product(self, name, category, price, quantity, aisle, bay):
        """Thêm sản phẩm mới"""
        try:
            # Kiểm tra tính hợp lệ của aisle và bay
            if not self._validate_location(aisle, bay):
                return False, "Invalid aisle or bay location"
                
            self.cursor.execute('''
                INSERT INTO products (name, category, price, quantity, aisle, bay)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, category, price, quantity, aisle.upper(), bay))
            
            self.conn.commit()
            self.product_cache.clear()
            
            # Lưu lịch sử
            self.change_history.append((
                'add',
                self.cursor.lastrowid,
                datetime.now(),
                {'name': name, 'category': category, 'aisle': aisle, 'bay': bay}
            ))
            return True, "Product added successfully"
        except Exception as e:
            return False, f"Error adding product: {str(e)}"

    def update_product(self, product_id, name, category, price, quantity, aisle, bay):
        """Cập nhật thông tin sản phẩm"""
        try:
            # Kiểm tra tính hợp lệ của aisle và bay
            if not self._validate_location(aisle, bay):
                return False, "Invalid aisle or bay location"
                
            self.cursor.execute('''
                UPDATE products 
                SET name = ?, category = ?, price = ?, quantity = ?, aisle = ?, bay = ?
                WHERE id = ?
            ''', (name, category, price, quantity, aisle.upper(), bay, product_id))
            
            self.conn.commit()
            self.product_cache.clear()
            
            # Lưu lịch sử
            old_data = self.get_product(product_id)
            self.change_history.append((
                'update',
                product_id,
                datetime.now(),
                {'old': old_data, 'new': (name, category, price, quantity, aisle, bay)}
            ))
            return True, "Product updated successfully"
        except Exception as e:
            return False, f"Error updating product: {str(e)}"

    def delete_product(self, product_id):
        """Xóa sản phẩm"""
        try:
            # Kiểm tra sản phẩm có tồn tại không
            if not self.get_product(product_id):
                return False, "Product not found"
                
            # Xóa sản phẩm
            self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
            self.conn.commit()
            
            # Xóa khỏi cache
            if product_id in self.product_cache:
                del self.product_cache[product_id]
                
            return True, "Product deleted successfully"
        except Exception as e:
            return False, f"Error deleting product: {str(e)}"

    def _validate_location(self, aisle, bay):
        """Kiểm tra tính hợp lệ của vị trí"""
        # Kiểm tra aisle (A-F)
        if not aisle.upper() in ['A', 'B', 'C', 'D', 'E', 'F']:
            return False
        
        # Kiểm tra bay (1-20)
        try:
            bay_num = int(bay)
            if not 1 <= bay_num <= 20:
                return False
        except ValueError:
            return False
            
        return True

    def get_product(self, product_id):
        """Lấy thông tin sản phẩm"""
        if product_id in self.product_cache:
            cached = self.product_cache[product_id]
            return (
                product_id,
                cached['name'],
                cached['category'],
                cached['price'],
                cached['quantity'],
                cached['aisle'],
                cached['bay']
            )
        
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        product = self.cursor.fetchone()
        if product:
            # Cache the product data
            self.product_cache[product_id] = {
                'name': product[1],
                'category': product[2],
                'price': product[3],
                'quantity': product[4],
                'aisle': product[5],
                'bay': product[6]
            }
        return product

    def get_all_products(self):
        """Lấy tất cả sản phẩm"""
        self.cursor.execute('SELECT * FROM products')
        products = self.cursor.fetchall()
        
        # Update cache
        for product in products:
            self.product_cache[product[0]] = {
                'name': product[1],
                'category': product[2],
                'price': product[3],
                'quantity': product[4],
                'aisle': product[5],
                'bay': product[6]
            }
        
        return products

    def search_products(self, keyword):
        """Tìm kiếm sản phẩm"""
        keyword = f"%{keyword}%"
        self.cursor.execute('''
            SELECT * FROM products 
            WHERE name LIKE ? OR category LIKE ?
        ''', (keyword, keyword))
        return self.cursor.fetchall()

    def get_low_quantity_products(self):
        """Lấy danh sách sản phẩm có số lượng thấp (dưới 10)"""
        self.cursor.execute('SELECT * FROM products WHERE quantity < 10')
        return self.cursor.fetchall()

    def get_products_by_location(self, aisle, bay):
        """Lấy sản phẩm theo vị trí"""
        self.cursor.execute('''
            SELECT * FROM products 
            WHERE aisle = ? AND bay = ?
        ''', (aisle.upper(), bay))
        return self.cursor.fetchall()

    def get_inventory_value(self):
        """Tính tổng giá trị hàng tồn kho"""
        self.cursor.execute('''
            SELECT SUM(price * quantity) 
            FROM products
        ''')
        result = self.cursor.fetchone()[0]
        return result if result is not None else 0.0

    def get_category_stats(self):
        """Lấy thống kê theo danh mục"""
        return self.category_manager.get_category_stats()

    def __del__(self):
        """Đóng kết nối khi đối tượng bị hủy"""
        self.conn.close() 