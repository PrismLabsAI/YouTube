# NanoClaw vs OpenClaw: Why NanoClaw Wins

> **[Watch on YouTube](https://youtu.be/QQNlk8380Ho)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# NanoClaw AI Agent Framework Companion Code

This repository provides real, working code examples to complement the YouTube video 'NanoClaw vs OpenClaw: Why NanoClaw Wins' by Prism Labs AI. NanoClaw is a lightweight, efficient AI agent framework designed for speed and simplicity.

## Files Overview

- `requirements.txt`: Lists the Python dependencies needed to run the examples.
- `nanoclaw.py`: Core NanoClaw framework implementation – a simple, functional AI agent runner using OpenAI's API.
- `example_agent.py`: Example script demonstrating how to create and run a basic web-scraping agent.
- `benchmark.py`: Script to benchmark agent performance on sample tasks.
- `config.yaml`: Example configuration file for an agent.
- `deploy.py`: Simple deployment script to run the agent as a web service using Flask.

## Setup

1. Clone this repository:
   ```bash
   git clone <this-repo-url>
   cd nanoclaw-companion
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   (Replace 'your-api-key-here' with your actual key.)

## How to Run

### Running an Example Agent

Execute the example agent:
```bash
python example_agent.py
```
This will run a simple reasoning task and output results.

### Benchmarking

Run benchmarks:
```bash
python benchmark.py
```
This compares execution times for sample tasks.

### Deploying as a Web Service

Deploy the agent:
```bash
python deploy.py
```
Then visit `http://localhost:5000` to interact with the agent via a simple web interface.

## Notes

- All code uses real packages (e.g., openai, requests, pyyaml).
- Error handling is included for common issues like missing API keys.
- This is a simplified implementation for educational purposes; the full NanoClaw framework is available via `pip install nanoclaw` as shown in the video.
- Ensure you have Python 3.8+ installed.

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
