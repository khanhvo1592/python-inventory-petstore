import customtkinter as ctk
from tkinter import ttk

class StatsTab:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory
        self.setup_ui()

    def setup_ui(self):
        """Thiết lập giao diện thống kê"""
        # Frame chính
        main_frame = ctk.CTkFrame(self.parent, fg_color="#121212", border_width=0)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Tiêu đề
        ctk.CTkLabel(
            main_frame,
            text="Inventory Statistics",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        ).pack(pady=20)

        # Frame cho các thống kê
        stats_frame = ctk.CTkFrame(main_frame, fg_color="#121212", border_width=0)
        stats_frame.pack(fill="both", expand=True)

        # Thống kê theo danh mục
        category_frame = ctk.CTkFrame(stats_frame, fg_color="#1e1e1e", border_width=0)
        category_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            category_frame,
            text="Products by Category",
            font=("Helvetica", 14, "bold"),
            text_color="white"
        ).pack(pady=10)

        # Treeview hiển thị thống kê danh mục
        self.category_tree = ttk.Treeview(
            category_frame,
            columns=("Category", "Count", "Total Value"),
            show="headings",
            height=10
        )
        self.category_tree.heading("Category", text="Category", anchor="w")
        self.category_tree.heading("Count", text="Count", anchor="w")
        self.category_tree.heading("Total Value", text="Total Value ($)", anchor="w")
        self.category_tree.column("Category", width=200, anchor="w")
        self.category_tree.column("Count", width=100, anchor="w")
        self.category_tree.column("Total Value", width=150, anchor="w")
        self.category_tree.pack(fill="x", padx=10, pady=10)

        # Thêm thanh cuộn cho category tree
        category_scrollbar = ttk.Scrollbar(category_frame, orient="vertical", command=self.category_tree.yview)
        category_scrollbar.pack(side="right", fill="y")
        self.category_tree.configure(yscrollcommand=category_scrollbar.set)

        # Thống kê tổng giá trị
        value_frame = ctk.CTkFrame(stats_frame, fg_color="#1e1e1e", border_width=0)
        value_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            value_frame,
            text="Total Inventory Value",
            font=("Helvetica", 14, "bold"),
            text_color="white"
        ).pack(pady=10)

        self.total_value_label = ctk.CTkLabel(
            value_frame,
            text="$0.00",
            font=("Helvetica", 24),
            text_color="white"
        )
        self.total_value_label.pack(pady=10)

        # Thống kê sản phẩm sắp hết hàng
        low_stock_frame = ctk.CTkFrame(stats_frame, fg_color="#1e1e1e", border_width=0)
        low_stock_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            low_stock_frame,
            text="Low Stock Products (Quantity < 10)",
            font=("Helvetica", 14, "bold"),
            text_color="white"
        ).pack(pady=10)

        self.low_stock_tree = ttk.Treeview(
            low_stock_frame,
            columns=("ID", "Name", "Category", "Quantity", "Aisle", "Bay"),
            show="headings",
            height=10
        )
        self.low_stock_tree.heading("ID", text="ID", anchor="w")
        self.low_stock_tree.heading("Name", text="Product Name", anchor="w")
        self.low_stock_tree.heading("Category", text="Category", anchor="w")
        self.low_stock_tree.heading("Quantity", text="Quantity", anchor="w")
        self.low_stock_tree.heading("Aisle", text="Aisle", anchor="w")
        self.low_stock_tree.heading("Bay", text="Bay", anchor="w")
        
        # Set column widths and alignment
        self.low_stock_tree.column("ID", width=50, anchor="w")
        self.low_stock_tree.column("Name", width=200, anchor="w")
        self.low_stock_tree.column("Category", width=150, anchor="w")
        self.low_stock_tree.column("Quantity", width=100, anchor="w")
        self.low_stock_tree.column("Aisle", width=50, anchor="w")
        self.low_stock_tree.column("Bay", width=50, anchor="w")
        
        self.low_stock_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add scrollbar for low stock tree
        low_stock_scrollbar = ttk.Scrollbar(low_stock_frame, orient="vertical", command=self.low_stock_tree.yview)
        low_stock_scrollbar.pack(side="right", fill="y")
        self.low_stock_tree.configure(yscrollcommand=low_stock_scrollbar.set)

        # Nút làm mới
        ctk.CTkButton(
            stats_frame,
            text="Refresh Statistics",
            command=self.refresh_stats,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(pady=20)

        # Làm mới dữ liệu ban đầu
        self.refresh_stats()

    def refresh_stats(self):
        """Làm mới tất cả thống kê"""
        # Xóa dữ liệu cũ
        for item in self.category_tree.get_children():
            self.category_tree.delete(item)
        for item in self.low_stock_tree.get_children():
            self.low_stock_tree.delete(item)

        # Lấy tất cả sản phẩm
        all_products = self.inventory.get_all_products()
        
        # Tính toán thống kê theo danh mục
        category_stats = {}
        for product in all_products:
            category = product[2]  # category is at index 2
            if category not in category_stats:
                category_stats[category] = {
                    'count': 0,
                    'total_value': 0
                }
            category_stats[category]['count'] += 1
            category_stats[category]['total_value'] += product[3] * product[4]  # price * quantity

        # Hiển thị thống kê theo danh mục
        for category, stats in category_stats.items():
            self.category_tree.insert(
                "", "end",
                values=(
                    category,
                    stats['count'],
                    f"${stats['total_value']:,.2f}"
                )
            )

        # Cập nhật tổng giá trị
        total_value = sum(stats['total_value'] for stats in category_stats.values())
        self.total_value_label.configure(text=f"${total_value:,.2f}")

        # Cập nhật sản phẩm sắp hết hàng
        low_stock_products = self.inventory.get_low_quantity_products()
        if low_stock_products:
            for product in low_stock_products:
                self.low_stock_tree.insert(
                    "", "end",
                    values=(
                        product[0],  # ID
                        product[1],  # Name
                        product[2],  # Category
                        product[4],  # Quantity
                        product[5],  # Aisle
                        product[6]   # Bay
                    ),
                    tags=('low_quantity',)
                )
        else:
            self.low_stock_tree.insert("", "end", values=("No low stock products found", "", "", "", "", ""))
            
        # Cấu hình tag cho sản phẩm có số lượng thấp
        self.low_stock_tree.tag_configure('low_quantity', background='#ffff99', foreground='black') 