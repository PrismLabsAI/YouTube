# OpenClaw 2026.3.8: SSRF Fixes & Hardening

> **[Watch on YouTube](https://youtu.be/2MrfWS9vUgo)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# OpenClaw 2026.3.8 Companion Code Examples

This repository provides real, working Python code examples that demonstrate key features from the OpenClaw 2026.3.8 release video. These scripts are beginner-friendly, include error handling, and can be cloned and run immediately.

## Files Overview

- **backup_verify.py**: Simulates the CLI backup/verify functionality using SHA-256 hashing for tamper-proof operations.
- **brave_search.py**: Demonstrates Brave-powered LLM-context web search for threat intelligence, using the Brave Search API and OpenAI for contextualization.
- **ssrf_protection.py**: Illustrates basic SSRF protection by validating origins and blocking unauthorized requests.
- **requirements.txt**: Lists the required Python packages.

## Setup

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set environment variables:
   - For `brave_search.py`: Set `BRAVE_API_KEY` (get from Brave Search API) and `OPENAI_API_KEY` (get from OpenAI).

## Running the Examples

- **Backup/Verify**: Run `python backup_verify.py` to create a backup with hash and verify it.
- **Brave Search**: Run `python brave_search.py` with a query like `python brave_search.py "latest SSRF exploits"`.
- **SSRF Protection**: Run `python ssrf_protection.py` to test origin validation.

These examples complement the video's demos, providing hands-on code for DevOps and cybersecurity pros.

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
