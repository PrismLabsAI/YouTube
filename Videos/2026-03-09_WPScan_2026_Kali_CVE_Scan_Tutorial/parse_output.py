# parse_output.py
# Script to parse WPScan JSON output and summarize vulnerabilities
# Usage: python parse_output.py <json_file>

import json
import sys
import os

# Check if file is provided
if len(sys.argv) != 2:
    print("Usage: python parse_output.py <json_file>")
    sys.exit(1)

json_file = sys.argv[1]

# Check if file exists
if not os.path.exists(json_file):
    print(f"Error: File '{json_file}' not found.")
    sys.exit(1)

# Load JSON data
try:
    with open(json_file, 'r') as f:
        data = json.load(f)
except json.JSONDecodeError:
    print("Error: Invalid JSON file.")
    sys.exit(1)

# Extract vulnerabilities
vulnerabilities = []
if 'plugins' in data:
    for plugin, details in data['plugins'].items():
        if 'vulnerabilities' in details:
            for vuln in details['vulnerabilities']:
                vulnerabilities.append({
                    'type': 'plugin',
                    'name': plugin,
                    'title': vuln.get('title', 'Unknown'),
                    'cve': vuln.get('cve', 'N/A'),
                    'cvss': vuln.get('cvss', {}).get('score', 'N/A')
                })

if 'themes' in data:
    for theme, details in data['themes'].items():
        if 'vulnerabilities' in details:
            for vuln in details['vulnerabilities']:
                vulnerabilities.append({
                    'type': 'theme',
                    'name': theme,
                    'title': vuln.get('title', 'Unknown'),
                    'cve': vuln.get('cve', 'N/A'),
                    'cvss': vuln.get('cvss', {}).get('score', 'N/A')
                })

# Print summary
print(f"Found {len(vulnerabilities)} vulnerabilities:")
for vuln in vulnerabilities:
    print(f"- {vuln['type'].capitalize()}: {vuln['name']} - {vuln['title']} (CVE: {vuln['cve']}, CVSS: {vuln['cvss']})")

if not vulnerabilities:
    print("No vulnerabilities found.")
