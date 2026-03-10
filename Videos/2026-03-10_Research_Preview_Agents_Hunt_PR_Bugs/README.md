# Research Preview: Agents Hunt PR Bugs

> **[Watch on YouTube](https://youtu.be/71uD5dNDCPQ)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# AI-Powered Code Review Agent Simulator

This repository provides a companion code example for the Prism Labs AI YouTube video on Anthropic's Claude Code Review. It simulates an agent-based code review system using AI (via OpenAI's API) to hunt bugs in parallel, verify findings, and rank them by severity.

## Features
- **Parallel Bug Hunting**: Simulates multiple AI agents reviewing code concurrently.
- **Verification**: Filters out false positives by cross-checking findings.
- **Severity Ranking**: Ranks bugs from 1-10 based on impact.
- **Auto-Fix Suggestions**: Generates and applies simple fixes.
- **CLI Interface**: Mimics commands like `claude pr-review rank` for ease of use.

## Files Overview
- `code_review_agent.py`: Main Python script implementing the CLI tool and agent logic.
- `requirements.txt`: Lists required Python packages.
- `sample_buggy_code.py`: A sample Python file with intentional bugs for demonstration.

## Setup
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your OpenAI API key as an environment variable: `export OPENAI_API_KEY='your-key-here'`

## Usage
### Review a File
Run: `python code_review_agent.py review sample_buggy_code.py`

This dispatches agents to hunt bugs in parallel.

### Rank Findings
After review, run: `python code_review_agent.py rank`

Displays ranked bugs with severity scores and evidence.

### Apply a Fix
Run: `python code_review_agent.py fix --issue 1`

Applies the suggested fix for the specified issue (requires manual confirmation in real scenarios).

## Notes
- This is a simulation using OpenAI's GPT model; it doesn't connect to real Claude Code.
- Bugs are detected via AI prompts; results may vary.
- For production use, integrate with actual CI/CD pipelines.
- Beginner-friendly: Comments in code explain each step.

Enjoy exploring AI-driven code review!

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
