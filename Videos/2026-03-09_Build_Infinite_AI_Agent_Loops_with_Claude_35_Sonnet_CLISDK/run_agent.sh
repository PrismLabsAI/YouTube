#!/bin/bash

# Script to run the Claude Code Loop agent in the background using screen

# Check if screen is installed
if ! command -v screen &> /dev/null; then
    echo "screen is not installed. Install it with: sudo apt-get install screen (Ubuntu) or brew install screen (macOS)"
    exit 1
fi

# Check if ANTHROPIC_API_KEY is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "ANTHROPIC_API_KEY environment variable not set. Please set it first."
    exit 1
fi

# Run the agent in a detached screen session
echo "Starting Claude Code Loop agent in background..."
screen -S claude-agent -d -m python agent.py

echo "Agent started. To attach to the session: screen -r claude-agent"
echo "To stop: Attach and press Ctrl+C, or run: screen -S claude-agent -X quit"