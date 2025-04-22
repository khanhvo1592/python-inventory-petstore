import customtkinter as ctk
from tkinter import ttk
from database.inventory import Inventory
from ui.styles import configure_styles
from ui.product_tab import ProductTab
from ui.stats_tab import StatsTab
from ui.product_form import ProductForm

class InventoryApp:
    def __init__(self):
        # Set appearance mode and theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.app = ctk.CTk()
        self.app.title("Pet Store Inventory Management")
        self.app.geometry("1200x800")
        self.app.configure(fg_color="#121212")
        
        # Initialize database
        self.inventory = Inventory()
        
        # Configure styles
        configure_styles()
        
        self.setup_ui()

    def setup_ui(self):
        # Set app icon
        try:
            self.app.iconbitmap("pet_store.ico")
        except:
            passd

        # Create main frame
        self.main_frame = ctk.CTkFrame(self.app, fg_color="#121212", border_width=0)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create left panel for product form
        self.left_panel = ctk.CTkFrame(self.main_frame, fg_color="#121212", border_width=0)
        self.left_panel.pack(side="left", fill="y", padx=10, pady=10)

        # Create right panel for tabs
        self.right_panel = ctk.CTkFrame(self.main_frame, fg_color="#121212", border_width=0)
        self.right_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.right_panel)
        self.notebook.pack(fill="both", expand=True, padx=0, pady=0)

        # Create Product List Tab
        self.product_tab = ctk.CTkFrame(self.notebook, fg_color="#121212", border_width=0)
        self.notebook.add(self.product_tab, text="Product List")
        self.product_list = ProductTab(self.product_tab, self.inventory)

        # Create Statistics Tab
        self.stats_tab = ctk.CTkFrame(self.notebook, fg_color="#121212", border_width=0)
        self.notebook.add(self.stats_tab, text="Statistics")
        self.stats = StatsTab(self.stats_tab, self.inventory)

        # Create Product Form
        self.product_form = ProductForm(
            self.left_panel,
            self.inventory,
            self.refresh_all
        )

    def refresh_all(self):
        """Refresh all components that display data"""
        self.product_list.refresh_products()
        self.stats.refresh_stats()

    def run(self):
        """Start the application"""
        self.app.mainloop()

def main():
    app = InventoryApp()
    app.run()

if __name__ == "__main__":
    main() 