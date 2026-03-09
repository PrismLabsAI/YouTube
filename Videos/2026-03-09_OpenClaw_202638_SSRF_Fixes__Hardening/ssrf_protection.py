# ssrf_protection.py
# Demonstrates basic SSRF protection by validating request origins,
# inspired by OpenClaw 2026.3.8 browser SSRF/CDP fixes.

import requests
import sys

ALLOWED_ORIGINS = ['https://trusted.example.com', 'http://localhost']

def validate_origin(url):
    """Check if the URL origin is allowed to prevent SSRF."""
    try:
        response = requests.head(url, timeout=5)
        origin = response.url.split('//')[0] + '//' + response.url.split('//')[1].split('/')[0]
        if origin not in ALLOWED_ORIGINS:
            return False, f"Blocked: Invalid origin {origin}"
        return True, "Origin validated"
    except requests.RequestException as e:
        return False, f"Request failed: {e}"

def test_exploit(url):
    """Simulate testing an exploit attempt."""
    valid, message = validate_origin(url)
    if valid:
        print(f"{message}: Request allowed.")
    else:
        print(f"Exploit attempt detected: {message}")
        print("Log: SSRF prevention triggered")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ssrf_protection.py <url_to_test>")
        sys.exit(1)
    
    url = sys.argv[1]
    test_exploit(url)
