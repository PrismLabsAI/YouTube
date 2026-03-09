#!/usr/bin/env python3

"""
WPScan Automation Script

This script automates running WPScan on a target URL, saves the output to a JSON file,
and prints a basic summary. It uses the WPScan API token from environment variables.

Usage: python wpscan_automate.py --url <target_url> [--output <output_file>]
"""

import argparse
import json
import os
import subprocess
import sys

# Function to run WPScan and capture output
def run_wpscan(url, output_file):
    api_token = os.environ.get('WPSCAN_API_TOKEN')
    if not api_token:
        print("Error: WPSCAN_API_TOKEN environment variable not set. Get one from wpscan.com.")
        sys.exit(1)
    
    # Build command with basic enumeration
    cmd = [
        'wpscan',
        '--url', url,
        '--enumerate', 'vp,vt,u',
        '--api-token', api_token,
        '--format', 'json',
        '--output', output_file
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"WPScan completed. Output saved to {output_file}.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running WPScan: {e}")
        print(f"Stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: WPScan not found. Ensure it's installed.")
        return False

# Function to parse and summarize JSON output
def summarize_output(output_file):
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        # Basic summary
        print("\n--- Scan Summary ---")
        if 'version' in data:
            print(f"WordPress Version: {data['version']['number']}")
        if 'plugins' in data:
            print(f"Vulnerable Plugins: {len(data['plugins'])}")
        if 'themes' in data:
            print(f"Vulnerable Themes: {len(data['themes'])}")
        if 'users' in data:
            print(f"Users Found: {len(data['users'])}")
        print("Run parse_cves.py for detailed CVE filtering.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error parsing output: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate WPScan scans.")
    parser.add_argument('--url', required=True, help='Target WordPress URL')
    parser.add_argument('--output', default='wpscan_results.json', help='Output JSON file')
    args = parser.parse_args()
    
    if run_wpscan(args.url, args.output):
        summarize_output(args.output)