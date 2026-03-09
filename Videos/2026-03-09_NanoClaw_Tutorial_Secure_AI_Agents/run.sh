#!/bin/bash
# Run Script for NanoClaw Agent
# Initializes, builds, and starts the agent.

set -e  # Exit on error

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo "Error: .env file not found. Please create it from .env.example."
    exit 1
fi

# Initialize agent
nanoclaw init myagent

# Copy config files to agent directory
cp config.yaml myagent/
cp docker-compose.yml myagent/
cp agent_tools.py myagent/

# Run the agent
cd myagent
nanoclaw run

echo "Agent is running on http://localhost:8080"
