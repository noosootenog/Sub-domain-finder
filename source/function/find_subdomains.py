# source/function/find_subdomains.py
import socket
from .load_wordlist import load_wordlist  # Import from same folder

def find_subdomains(domain: str):
    """
    Finds subdomains using DNS resolution.
    Returns list of (subdomain, ip) tuples.
    """
    wordlist = load_wordlist()
    if not wordlist:
        return []
    
    domain = domain.strip().lower()
    if not domain:
        return []

    results = []
    for sub in wordlist:
        full_subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_subdomain)
            results.append((full_subdomain, ip))
        except socket.gaierror:
            pass
        except Exception as e:
            print(f"Error checking {full_subdomain}: {e}")
            pass
    return results