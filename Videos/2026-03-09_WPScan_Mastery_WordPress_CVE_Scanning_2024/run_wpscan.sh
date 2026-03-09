#!/bin/bash

# WPScan Quick Run Script
# This script runs a basic WPScan scan on a given URL with enumeration options.
# Assumes WPScan is installed and WPSCAN_API_TOKEN is set.

# Check if URL is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target_url>"
    echo "Example: $0 https://target.example.com"
    exit 1
fi

TARGET_URL=$1
API_TOKEN=${WPSCAN_API_TOKEN:-""}

if [ -z "$API_TOKEN" ]; then
    echo "Error: WPSCAN_API_TOKEN environment variable not set."
    exit 1
fi

# Run WPScan with basic options
echo "Running WPScan on $TARGET_URL..."
wpscan --url "$TARGET_URL" --enumerate vp,vt,u --api-token "$API_TOKEN"

if [ $? -eq 0 ]; then
    echo "Scan completed. For advanced options, edit this script or use wpscan_automate.py."
else
    echo "Scan failed. Check URL and API token."
fi