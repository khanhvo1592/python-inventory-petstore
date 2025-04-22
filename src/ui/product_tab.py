import customtkinter as ctk
from tkinter import ttk, messagebox

class ProductTab:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory
        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface for the Product List"""
        # Main frame
        main_frame = ctk.CTkFrame(self.parent, fg_color="#121212", border_width=0)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Menu buttons frame
        menu_frame = ctk.CTkFrame(main_frame, fg_color="#121212", border_width=0)
        menu_frame.pack(fill="x", padx=10, pady=10)

        # Add menu buttons
        ctk.CTkButton(
            menu_frame,
            text="Update Selected",
            command=self.edit_product,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            menu_frame,
            text="Delete Selected",
            command=self.delete_product,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            menu_frame,
            text="Check Low Stock",
            command=self.check_low_stock,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)

        # Search section
        search_frame = ctk.CTkFrame(main_frame, fg_color="#121212", border_width=0)
        search_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            search_frame,
            text="Search:",
            text_color="white",
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            fg_color="#1e1e1e",
            border_color="#2d2d2d",
            text_color="white",
            height=35,
            font=("Helvetica", 12)
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.search_entry.bind("<KeyRelease>", self.on_search)

        ctk.CTkButton(
            search_frame,
            text="Clear",
            command=self.clear_search,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(side="left", padx=5)

        # Product list
        list_frame = ctk.CTkFrame(main_frame, fg_color="#121212", border_width=0)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create Treeview
        self.tree = ttk.Treeview(
            list_frame,
            columns=("ID", "Name", "Category", "Price", "Quantity", "Aisle", "Bay"),
            show="headings",
            height=20
        )

        # Define columns
        columns = {
            "ID": "Product ID",
            "Name": "Product Name",
            "Category": "Category",
            "Price": "Price",
            "Quantity": "Quantity",
            "Aisle": "Aisle",
            "Bay": "Bay"
        }

        for col, heading in columns.items():
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=100)

        self.tree.pack(fill="both", expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Load initial data
        self.refresh_products()

    def on_search(self, event):
        """Handle search input"""
        keyword = self.search_entry.get()
        if keyword:
            products = self.inventory.search_products(keyword)
        else:
            products = self.inventory.get_all_products()
        self.update_product_list(products)

    def clear_search(self):
        """Clear search and show all products"""
        self.search_entry.delete(0, "end")
        self.refresh_products()

    def refresh_products(self):
        """Refresh the product list"""
        products = self.inventory.get_all_products()
        self.update_product_list(products)

    def update_product_list(self, products):
        """Update the product list display"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add new items
        for product in products:
            # Kiểm tra số lượng thấp
            if product[4] < 10:  # quantity < 10
                self.tree.insert("", "end", values=product, tags=('low_quantity',))
            else:
                self.tree.insert("", "end", values=product)

        # Cấu hình tag cho sản phẩm có số lượng thấp
        self.tree.tag_configure('low_quantity', background='#ffff99', foreground='black')

    def edit_product(self):
        """Edit selected product"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a product to edit")
            return

        item = self.tree.item(selected[0])
        product_id = item['values'][0]

        # Create edit window
        edit_window = ctk.CTkToplevel(self.parent)
        edit_window.title("Edit Product")
        edit_window.geometry("400x600")  # Increased height
        edit_window.grab_set()  # Modal window

        # Create main frame with padding
        main_frame = ctk.CTkFrame(edit_window, fg_color="#121212")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Get current product data
        product = self.inventory.get_product(product_id)
        if not product:
            messagebox.showerror("Error", "Product not found")
            return

        # Create form with proper spacing
        ctk.CTkLabel(main_frame, text="Name:", text_color="white").pack(pady=(10, 5))
        name_entry = ctk.CTkEntry(main_frame)
        name_entry.insert(0, product[1])
        name_entry.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(main_frame, text="Category:", text_color="white").pack(pady=(10, 5))
        category_entry = ctk.CTkEntry(main_frame)
        category_entry.insert(0, product[2])
        category_entry.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(main_frame, text="Price:", text_color="white").pack(pady=(10, 5))
        price_entry = ctk.CTkEntry(main_frame)
        price_entry.insert(0, str(product[3]))
        price_entry.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(main_frame, text="Quantity:", text_color="white").pack(pady=(10, 5))
        quantity_entry = ctk.CTkEntry(main_frame)
        quantity_entry.insert(0, str(product[4]))
        quantity_entry.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(main_frame, text="Aisle:", text_color="white").pack(pady=(10, 5))
        aisle_entry = ctk.CTkEntry(main_frame)
        aisle_entry.insert(0, product[5])
        aisle_entry.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(main_frame, text="Bay:", text_color="white").pack(pady=(10, 5))
        bay_entry = ctk.CTkEntry(main_frame)
        bay_entry.insert(0, str(product[6]))
        bay_entry.pack(fill="x", pady=(0, 10))

        # Create button frame
        button_frame = ctk.CTkFrame(main_frame, fg_color="#121212")
        button_frame.pack(fill="x", pady=20)

        def save_changes():
            try:
                name = name_entry.get()
                category = category_entry.get()
                price = float(price_entry.get())
                quantity = int(quantity_entry.get())
                aisle = aisle_entry.get()
                bay = int(bay_entry.get())

                if not all([name, category, aisle]):
                    messagebox.showerror("Error", "All fields are required")
                    return

                success, message = self.inventory.update_product(product_id, name, category, price, quantity, aisle, bay)
                if success:
                    self.refresh_products()
                    edit_window.destroy()
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)

            except ValueError:
                messagebox.showerror("Error", "Invalid input values")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Add Save and Cancel buttons
        ctk.CTkButton(
            button_frame,
            text="Save Changes",
            command=save_changes,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(side="left", padx=5, expand=True)

        ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=edit_window.destroy,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(side="right", padx=5, expand=True)

    def delete_product(self):
        """Xóa sản phẩm đã chọn"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a product to delete")
            return
            
        product_id = self.tree.item(selected[0])['values'][0]
        product_name = self.tree.item(selected[0])['values'][1]
        
        # Xác nhận xóa
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {product_name}?"):
            try:
                # Gọi phương thức xóa từ inventory
                success, message = self.inventory.delete_product(product_id)
                
                if success:
                    # Xóa item khỏi treeview
                    self.tree.delete(selected[0])
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete product: {str(e)}")

    def check_low_stock(self):
        """Kiểm tra và hiển thị sản phẩm có số lượng thấp"""
        low_stock_products = self.inventory.get_low_quantity_products()
        
        if not low_stock_products:
            messagebox.showinfo("Low Stock Check", "No products with low stock found")
            return
            
        # Tạo cửa sổ hiển thị sản phẩm có số lượng thấp
        low_stock_window = ctk.CTkToplevel(self.parent)
        low_stock_window.title("Low Stock Products")
        low_stock_window.geometry("800x400")
        low_stock_window.grab_set()
        
        # Tạo frame chứa danh sách
        list_frame = ctk.CTkFrame(low_stock_window, fg_color="#121212", border_width=0)
        list_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Tạo Treeview
        low_stock_tree = ttk.Treeview(
            list_frame,
            columns=("ID", "Name", "Category", "Price", "Quantity", "Aisle", "Bay"),
            show="headings",
            height=15
        )
        
        # Định nghĩa cột
        columns = {
            "ID": "Product ID",
            "Name": "Product Name",
            "Category": "Category",
            "Price": "Price",
            "Quantity": "Quantity",
            "Aisle": "Aisle",
            "Bay": "Bay"
        }
        
        for col, heading in columns.items():
            low_stock_tree.heading(col, text=heading)
            low_stock_tree.column(col, width=100)
            
        low_stock_tree.pack(fill="both", expand=True)
        
        # Thêm thanh cuộn
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=low_stock_tree.yview)
        scrollbar.pack(side="right", fill="y")
        low_stock_tree.configure(yscrollcommand=scrollbar.set)
        
        # Thêm sản phẩm vào treeview
        for product in low_stock_products:
            low_stock_tree.insert("", "end", values=product, tags=('low_quantity',))
            
        # Cấu hình tag cho sản phẩm có số lượng thấp
        low_stock_tree.tag_configure('low_quantity', background='#ffff99', foreground='black')
        
        # Thêm nút đóng
        ctk.CTkButton(
            list_frame,
            text="Close",
            command=low_stock_window.destroy,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(pady=10) 