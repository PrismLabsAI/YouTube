# Claude Code Loop: Build 24/7 AI Agents!

> **[Watch on YouTube](https://youtu.be/fLoO6mA_bjY)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# Claude Code Loop: Build 24/7 AI Agents

This repository provides companion code for the YouTube video on building 24/7 AI agents using Claude's code loop command with Claude 3.5 Sonnet.

## Files Overview

- `package.json`: Node.js project configuration with dependencies.
- `index.js`: Core code loop template for autonomous agents using the Anthropic SDK.
- `bitcoin_agent.js`: Example agent that monitors Bitcoin price and alerts on significant changes.
- `content_generator_agent.js`: Example agent that generates daily Twitter thread ideas on AI news.
- `.env.example`: Template for environment variables (copy to `.env` and fill in your keys).

## Setup

1. Clone this repository.
2. Run `npm install` to install dependencies.
3. Copy `.env.example` to `.env` and add your Anthropic API key (get it from console.anthropic.com).
4. Customize the agent scripts as needed.

## Running Locally

- To run the core template: `node index.js`
- To run the Bitcoin agent: `node bitcoin_agent.js`
- To run the content generator: `node content_generator_agent.js`

These agents will loop indefinitely. Use Ctrl+C to stop.

## Deployment

For 24/7 operation, deploy to Replit or Vercel:

- On Replit: Create a new Repl, upload these files, set environment variables in Secrets, and run the script.
- On Vercel: Use their Node.js deployment, set env vars in dashboard.

Note: Ensure your Anthropic account has sufficient usage limits.

## Requirements

- Node.js 16+
- Anthropic API key
- For Bitcoin agent: CoinGecko API (free, no key needed)

## Disclaimer

This is for educational purposes. Handle API usage responsibly and comply with terms of service.
## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
