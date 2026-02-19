import os

def load_wordlist():
    """
    Loads subdomain prefixes from wordlist.txt (dynamic path).
    Falls back to hardcoded list if file missing.
    """
    # Default hardcoded wordlist (for portability if file not found)
    default_wordlist = [
        "www", "mail", "ftp", "admin", "test", "dev", "api", "blog", "shop", "forum",
        "news", "webmail", "staging", "beta", "secure", "support", "portal", "vpn",
        "cms", "intranet", "extranet", "wiki", "git", "docs", "app", "login",
        "dashboard", "adminpanel", "cpanel", "db"
    ]
    
    # Dynamic path: Relative to this script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir,'..', '..','wordlist.txt')
    try:
        with open(file_path, 'r') as f:
            loaded = [line.strip().lower() for line in f if line.strip()]
            if loaded:
                return loaded  # Use file if not empty
            else:
                print("Warning: wordlist.txt is empty. Using default hardcoded list.")
                return default_wordlist
    except FileNotFoundError:
        print("Warning: wordlist.txt not found. Using default hardcoded list.")
        return default_wordlist
    except Exception as e:
        print(f"Error loading wordlist: {e}. Using default hardcoded list.")
        return default_wordlist
    
    
    
load_wordlist() 