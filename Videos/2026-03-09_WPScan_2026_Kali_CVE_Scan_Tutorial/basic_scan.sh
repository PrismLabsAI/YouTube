#!/bin/bash

# Basic WPScan enumeration script
# Usage: ./basic_scan.sh <target_url>

# Check if URL is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target_url>"
    exit 1
fi

TARGET_URL=$1
API_TOKEN=$WP_API_TOKEN

# Check if API token is set
if [ -z "$API_TOKEN" ]; then
    echo "Error: WP_API_TOKEN environment variable not set."
    echo "Set it with: export WP_API_TOKEN=your_token_here"
    exit 1
fi

# Run basic enumeration scan
wpscan --url "$TARGET_URL" --api-token "$API_TOKEN" --enumerate vp,vt --output basic_scan_output.txt

# Check if scan completed successfully
echo "Scan completed. Check basic_scan_output.txt for results."
