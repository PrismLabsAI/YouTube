# Build Infinite AI Agent Loops with Claude 3.5 Sonnet CLI/SDK

> **[Watch on YouTube](https://youtu.be/qxZ7fiJpP3o)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# Claude Code Loop: Autonomous AI Agent

This repository provides a companion code example for the YouTube video 'Build Infinite AI Agent Loops with Claude 3.5 Sonnet CLI/SDK'. It demonstrates how to build an autonomous AI agent using Claude 3.5 Sonnet that can generate code, execute it, self-improve, and run in a loop.

## What Each File Does

- `agent.py`: The main Python script that implements the Claude Code Loop. It uses the Anthropic SDK to prompt Claude for code generation, executes the code safely, logs results, and persists state.
- `requirements.txt`: Lists the Python dependencies needed to run the agent.
- `state.json`: Initial state file for the agent, containing tasks, logs, and metrics. This file is updated during execution.
- `run_agent.sh`: A shell script to run the agent in the background using `screen` for 24/7 operation.

## Setup

1. **Install Dependencies**:
   - Ensure you have Python 3.8+ installed.
   - Install the required packages: `pip install -r requirements.txt`
   - Optionally, install the Claude Code CLI for file editing: `npm install -g @anthropic/claude-code`

2. **Set Up API Key**:
   - Get your Anthropic API key from [console.anthropic.com](https://console.anthropic.com).
   - Set it as an environment variable: `export [REDACTED]
   - Do not hardcode it in the code.

3. **Initial State**:
   - The `state.json` file is pre-populated with an example task. You can edit it to add your own tasks.

## How to Run

### Basic Run (for testing)
- Run the agent once: `python agent.py`
- It will process one task, execute code, and update the state.

### Infinite Loop (24/7)
- Use the provided script to run it in the background: `./run_agent.sh`
- This detaches the process using `screen`. To reattach: `screen -r claude-agent`
- To stop: Attach to screen and press Ctrl+C, or kill the screen session.

### Using Claude Code CLI
- For manual editing: `claude code --edit agent.py --append "# Your code here"`
- But the agent itself uses the SDK for automation.

## Notes
- The code execution is sandboxed using `exec` with restricted builtins for safety, but avoid running untrusted code in production.
- The loop includes error handling and self-improvement prompts.
- For real-world use, monitor the `state.json` file for progress and logs.
- This is a demo; customize the prompts and tasks as needed.

## Disclaimer
- Running infinite loops can consume API credits. Monitor your usage.
- Ensure compliance with Anthropic's terms of service.

Enjoy building your never-sleeping AI agent!
## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
