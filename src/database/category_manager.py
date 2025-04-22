class CategoryManager:
    def __init__(self):
        # Dictionary để lưu trữ danh mục và số lượng sản phẩm
        self.categories = {
            "Dog Food": [],
            "Cat Food": [],
            "Toys": [],
            "Accessories": [],
            "Grooming": [],
            "Medicine": [],
            "Bedding": []
        }
        
        # List để lưu trữ lịch sử thay đổi danh mục
        self.category_history = []
        
        # Tuple chứa các danh mục mặc định
        self.default_categories = (
            "Dog Food", "Cat Food", "Toys", "Accessories",
            "Grooming", "Medicine", "Bedding"
        )

    def add_product_to_category(self, product_id, category):
        """Thêm sản phẩm vào danh mục"""
        if category in self.categories:
            self.categories[category].append(product_id)
            self.category_history.append(("add", product_id, category))
            return True
        return False

    def remove_product_from_category(self, product_id, category):
        """Xóa sản phẩm khỏi danh mục"""
        if category in self.categories and product_id in self.categories[category]:
            self.categories[category].remove(product_id)
            self.category_history.append(("remove", product_id, category))
            return True
        return False

    def get_products_in_category(self, category):
        """Lấy danh sách sản phẩm trong một danh mục"""
        return self.categories.get(category, [])

    def get_category_stats(self):
        """Lấy thống kê số lượng sản phẩm theo danh mục"""
        return {category: len(products) for category, products in self.categories.items()}

    def get_all_categories(self):
        """Lấy danh sách tất cả danh mục"""
        return list(self.categories.keys()) 