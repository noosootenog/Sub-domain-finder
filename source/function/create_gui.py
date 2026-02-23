import tkinter as tk
from tkinter import scrolledtext
from .start_scan import start_scan  # Import from same folder

def create_gui():
    """
    Creates and returns the GUI components.
    """
    root = tk.Tk()
    root.title("Subdomain Finder")
    root.geometry("650x500")
    root.resizable(True, True)

    tk.Label(root, text="Subdomain Finder", font=("Arial", 18, "bold")).pack(pady=15)

    tk.Label(root, text="Enter Target Domain (e.g., example.com):", font=("Arial", 12)).pack()
    entry_domain = tk.Entry(root, width=50, font=("Arial", 12), justify="center")
    entry_domain.pack(pady=8, ipady=4)

    scan_btn = tk.Button(root, text=" Start Scan", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", height=2, width=20,
                         command=lambda: start_scan(entry_domain, text_results, root))
    scan_btn.pack(pady=15)

    text_results = scrolledtext.ScrolledText(root, height=18, width=75, font=("Consolas", 10))
    text_results.pack(pady=10, padx=15)

    return root, entry_domain, text_results  