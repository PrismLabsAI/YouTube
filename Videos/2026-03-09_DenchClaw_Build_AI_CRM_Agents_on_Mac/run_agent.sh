#!/bin/bash

# Run Example Outreach Agent Script
# This script runs the 'leadhunter' agent on sample leads.
# Ensure DenchClaw is installed and initialized.
# Run with: ./run_agent.sh

set -e  # Exit on error

# Path to DenchClaw binary (adjust if needed)
DENCHCLAW_PATH="./target/release/denchclaw"

# Check if binary exists
if [ ! -f "$DENCHCLAW_PATH" ]; then
    echo "Error: DenchClaw binary not found at $DENCHCLAW_PATH. Please build it first."
    exit 1
fi

# Import leads (assuming sample_leads.csv is in the same directory)
echo "Importing sample leads..."
$DENCHCLAW_PATH leads import sample_leads.csv

# Run the agent
echo "Running outreach agent 'leadhunter' on 10 leads..."
$DENCHCLAW_PATH agent run leadhunter --leads 10

echo "Agent run complete. Check outputs for results."