from tkinter import ttk

def configure_styles():
    style = ttk.Style()
    
    # Base colors
    DARK_BG = "#121212"
    DARKER_BG = "#1e1e1e"
    HOVER_BG = "#2d2d2d"
    TEXT_COLOR = "white"
    
    # Common configuration
    common_config = {
        "borderwidth": 0,
        "relief": "flat"
    }
    
    # Configure Treeview
    style.configure(
        "Treeview",
        background=DARK_BG,
        foreground=TEXT_COLOR,
        fieldbackground=DARK_BG,
        rowheight=30,
        font=("Helvetica", 12),
        **common_config
    )
    style.configure(
        "Treeview.Heading",
        background=DARKER_BG,
        foreground=TEXT_COLOR,
        font=("Helvetica", 12, "bold"),
        **common_config
    )
    style.map(
        "Treeview",
        background=[("selected", HOVER_BG)],
        foreground=[("selected", TEXT_COLOR)]
    )
    
    # Configure Notebook
    style.configure(
        "TNotebook",
        background=DARK_BG,
        padding=0,
        **common_config
    )
    style.configure(
        "TNotebook.Tab",
        background=DARKER_BG,
        foreground=TEXT_COLOR,
        padding=[15, 5],
        font=("Helvetica", 12),
        **common_config
    )
    style.map(
        "TNotebook.Tab",
        background=[
            ("selected", DARK_BG),
            ("active", HOVER_BG)
        ],
        foreground=[("selected", TEXT_COLOR), ("active", TEXT_COLOR)],
        expand=[("selected", [0, 0, 0, 0])]
    )
    
    # Configure Frame
    style.configure(
        "TFrame",
        background=DARK_BG,
        **common_config
    )
    
    # Configure Scrollbar
    style.configure(
        "Vertical.TScrollbar",
        background=DARK_BG,
        arrowcolor=TEXT_COLOR,
        troughcolor=DARK_BG,
        width=12,
        **common_config
    )
    style.map(
        "Vertical.TScrollbar",
        background=[("active", HOVER_BG)],
        relief=[("active", "flat")]
    )
    
    # Configure Separator
    style.configure(
        "TSeparator",
        background=HOVER_BG
    )
    
    # Configure Label
    style.configure(
        "TLabel",
        background=DARK_BG,
        foreground=TEXT_COLOR,
        font=("Helvetica", 12),
        **common_config
    )
    
    # Configure Button
    style.configure(
        "TButton",
        background=DARKER_BG,
        foreground=TEXT_COLOR,
        font=("Helvetica", 12),
        **common_config
    )
    style.map(
        "TButton",
        background=[("active", HOVER_BG)],
        foreground=[("active", TEXT_COLOR), ("disabled", TEXT_COLOR)]
    )
    
    # Configure Entry
    style.configure(
        "TEntry",
        background=DARKER_BG,
        foreground=TEXT_COLOR,
        fieldbackground=DARKER_BG,
        font=("Helvetica", 12),
        **common_config
    )
    style.map(
        "TEntry",
        fieldbackground=[("readonly", DARKER_BG)],
        foreground=[("readonly", TEXT_COLOR)]
    )
    
    # Configure Combobox
    style.configure(
        "TCombobox",
        background=DARKER_BG,
        foreground=TEXT_COLOR,
        fieldbackground=DARKER_BG,
        arrowcolor=TEXT_COLOR,
        font=("Helvetica", 12),
        **common_config
    )
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", DARKER_BG)],
        foreground=[("readonly", TEXT_COLOR)]
    ) 