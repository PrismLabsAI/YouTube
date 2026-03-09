# NanoClaw Tutorial: Secure AI Agents

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# NanoClaw Sample Agent

This repository provides a sample setup for building a secure AI agent using NanoClaw. NanoClaw is a lightweight alternative to OpenClaw, running in containers for enhanced security. It integrates with messaging apps like WhatsApp, Telegram, Slack, Discord, and Gmail, supports persistent memory, scheduled jobs, and is built on Anthropic's Claude API with tool calling.

## Files Overview

- `README.md`: This file, explaining setup and usage.
- `config.yaml`: Sample configuration file for the NanoClaw agent, including API keys, integrations, and settings.
- `docker-compose.yml`: Docker Compose file to run the agent in a containerized environment.
- `agent_tools.py`: Python script defining custom tools for the agent using Anthropic's SDK.
- `requirements.txt`: List of Python dependencies required for the agent tools.
- `.env`: Environment variables file (copy from `.env.example` and fill in your keys).
- `run.sh`: Shell script to initialize and run the agent using NanoClaw CLI.

## Setup

1. **Install NanoClaw CLI**: Run `curl -fsSL https://get.nanoclaw.dev | bash` to install the CLI.

2. **Clone this repository**: `git clone <this-repo-url>` and navigate to the directory.

3. **Environment Variables**: Copy `.env.example` to `.env` and fill in your API keys:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key.
   - `SLACK_BOT_TOKEN`: Token for Slack integration.
   - `DISCORD_BOT_TOKEN`: Token for Discord integration.
   - Other keys as needed for integrations (e.g., WhatsApp, Gmail).

4. **Install Python Dependencies**: Run `pip install -r requirements.txt`.

5. **Configure Integrations**: Edit `config.yaml` to add your phone number for WhatsApp, channels for Slack/Discord, etc.

## Running the Agent

- **Using the Script**: Run `./run.sh` to initialize, build, and start the agent.

- **Manual Steps**:
  1. `nanoclaw init myagent` (creates scaffold).
  2. Copy `config.yaml` and `docker-compose.yml` to the agent directory.
  3. `nanoclaw run` to build and start the container.
  4. Add integrations: `nanoclaw add whatsapp --phone +1234567890`, `nanoclaw add slack`, etc.
  5. Enable memory: `nanoclaw memory enable`.
  6. Schedule jobs: `nanoclaw schedule '0 9 * * 1' 'send_weekly_report'`.

The agent will run on `http://localhost:8080` and connect to your specified integrations.

## Custom Tools

Edit `agent_tools.py` to define custom tools. For example, add functions for data fetching or calculations. The script uses Anthropic's SDK to handle tool calling.

## Security Note

All sensitive data is handled via environment variables. The containerized setup ensures isolation.

For more details, visit [nanoclaw.dev](https://nanoclaw.dev).


---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
