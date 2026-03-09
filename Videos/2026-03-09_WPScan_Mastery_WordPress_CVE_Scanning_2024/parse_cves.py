#!/usr/bin/env python3

"""
CVE Parser Script

Parses WPScan JSON output to filter and report high-severity CVEs (CVSS >= 7.0).

Usage: python parse_cves.py <wpscan_output.json>
"""

import json
import sys

# Function to filter CVEs
def filter_cves(data, min_cvss=7.0):
    critical_cves = []
    
    # Check plugins
    if 'plugins' in data:
        for plugin, details in data['plugins'].items():
            if 'vulnerabilities' in details:
                for vuln in details['vulnerabilities']:
                    if 'cvss' in vuln and vuln['cvss']['score'] >= min_cvss:
                        critical_cves.append({
                            'type': 'Plugin',
                            'name': plugin,
                            'title': vuln['title'],
                            'cve': vuln.get('cve', 'N/A'),
                            'cvss': vuln['cvss']['score']
                        })
    
    # Check themes (similar structure)
    if 'themes' in data:
        for theme, details in data['themes'].items():
            if 'vulnerabilities' in details:
                for vuln in details['vulnerabilities']:
                    if 'cvss' in vuln and vuln['cvss']['score'] >= min_cvss:
                        critical_cves.append({
                            'type': 'Theme',
                            'name': theme,
                            'title': vuln['title'],
                            'cve': vuln.get('cve', 'N/A'),
                            'cvss': vuln['cvss']['score']
                        })
    
    return critical_cves

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python parse_cves.py <wpscan_output.json>")
        sys.exit(1)
    
    output_file = sys.argv[1]
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        cves = filter_cves(data)
        if cves:
            print(f"Found {len(cves)} high-severity CVEs:")
            for cve in cves:
                print(f"- {cve['type']}: {cve['name']} - {cve['title']} (CVE: {cve['cve']}, CVSS: {cve['cvss']})")
        else:
            print("No high-severity CVEs found.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()