import os
import tkinter as tk
from .find_subdomains import find_subdomains  # Import from same folder

def perform_scan(domain, root, text_results):
    """
    Performs the subdomain scan in a background thread.
    Updates GUI and saves results if found.
    """
    root.after(0, lambda: text_results.insert(tk.END, f"🔍 Scanning subdomains for: {domain}\n\n"))
    root.after(0, text_results.update)

    results = find_subdomains(domain)
    
    if results:
        root.after(0, lambda: text_results.insert(tk.END, f"✅ Found {len(results)} subdomains:\n\n"))
        for subdomain, ip in results:
            root.after(0, lambda sub=subdomain, ip=ip: text_results.insert(tk.END, f"→ {sub}  →  {ip}\n"))
        
        os.makedirs('../../find', exist_ok=True)  # Adjusted path from subfolder
        with open('../../find/found_subdomains.txt', 'w', encoding='utf-8') as f:  # Added encoding='utf-8'
            for subdomain, ip in results:
                f.write(f"{subdomain} → {ip}\n")
        root.after(0, lambda: text_results.insert(tk.END, "\nResults saved to find/found_subdomains.txt\n"))
    else:
        root.after(0, lambda: text_results.insert(tk.END, "❌ No subdomains found. (Check assets/wordlist.txt?)\n"))
    
    root.after(0, text_results.update)