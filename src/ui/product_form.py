import customtkinter as ctk
from tkinter import messagebox

class ProductForm:
    def __init__(self, parent, inventory_manager, refresh_callback):
        """Initialize the Product Form"""
        self.parent = parent
        self.inventory = inventory_manager
        self.refresh_callback = refresh_callback
        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface for the Product Form"""
        # Create form frame
        form_frame = ctk.CTkFrame(self.parent, fg_color="#121212", border_width=0)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        ctk.CTkLabel(
            form_frame,
            text="Add New Product",
            font=("Helvetica", 16, "bold"),
            text_color="white"
        ).pack(pady=20)

        # Create input fields
        self.entries = {}
        fields = [
            ("id", "Product ID:"),
            ("name", "Product Name:"),
            ("category", "Category:"),
            ("price", "Price:"),
            ("quantity", "Quantity:"),
            ("aisle", "Aisle (A-F):"),
            ("bay", "Bay (1-20):")
        ]

        for field, label in fields:
            # Create frame for each input field
            input_frame = ctk.CTkFrame(form_frame, fg_color="#121212", border_width=0)
            input_frame.pack(fill="x", padx=20, pady=5)

            # Label
            ctk.CTkLabel(
                input_frame,
                text=label,
                text_color="white",
                font=("Helvetica", 12)
            ).pack(side="left")

            # Entry field
            entry = ctk.CTkEntry(
                input_frame,
                fg_color="#1e1e1e",
                border_color="#2d2d2d",
                text_color="white",
                height=35,
                font=("Helvetica", 12)
            )
            entry.pack(side="right", fill="x", expand=True)
            self.entries[field] = entry

        # Add button
        ctk.CTkButton(
            form_frame,
            text="Add Product",
            command=self.add_product,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2d2d2d",
            height=35,
            font=("Helvetica", 12)
        ).pack(pady=20)

    def add_product(self):
        """Add a new product to the inventory"""
        try:
            # Get values from entries
            name = self.entries["name"].get()
            category = self.entries["category"].get()
            price = float(self.entries["price"].get())
            quantity = int(self.entries["quantity"].get())
            aisle = self.entries["aisle"].get().upper()
            bay = self.entries["bay"].get()

            # Validate inputs
            if not all([name, category, aisle, bay]):
                messagebox.showerror("Error", "Please fill in all fields")
                return

            if price <= 0 or quantity < 0:
                messagebox.showerror("Error", "Please enter valid values for price and quantity")
                return

            # Add product to inventory
            success, message = self.inventory.add_product(
                name, category, price, quantity, aisle, bay
            )
            
            if success:
                # Clear form
                for entry in self.entries.values():
                    entry.delete(0, "end")
                # Refresh product list
                self.refresh_callback()
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid values for price and quantity")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}") 