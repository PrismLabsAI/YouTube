# health_check.py
# Script to check the health of an API endpoint.
# Usage: python health_check.py
# Set HEALTH_URL environment variable for custom endpoint.

import os
import requests

def check_health():
    url = os.environ.get('HEALTH_URL', 'https://api.example.com/health')
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"HTTP/{response.raw.version} {response.status_code} {response.reason}")
            print("Status: Healthy")
        else:
            print(f"HTTP/{response.raw.version} {response.status_code} {response.reason}")
            print("Status: Unhealthy - Alert needed!")
    except requests.RequestException as e:
        print(f"Error checking health: {e}")
        print("Status: Unhealthy - Alert needed!")

if __name__ == "__main__":
    check_health()
