import tkinter as tk
from tkinter import messagebox
import threading
from .perform_scan import perform_scan  # Import from same folder

def start_scan(entry_domain, text_results, root):
    domain = entry_domain.get().strip()
    
    if not domain:
        messagebox.showerror("Error", "Please enter a domain!")
        return
    
    text_results.delete(1.0, tk.END)
    
    threading.Thread(target=perform_scan, args=(domain, root, text_results)).start()