from function.load_wordlist import load_wordlist
from function.create_gui import create_gui

if __name__ == "__main__":
    
    wordlist = load_wordlist()
    if not wordlist:
        print("Warning: No wordlist loaded. Scans may return no results.")
    
    # Run GUI
    root, _, _ = create_gui()  # Get root (ignore others)
    root.mainloop()