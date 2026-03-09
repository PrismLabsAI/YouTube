# Claude Code /loop Command: Build 24/7 Autonomous Agents

> **[Watch on YouTube](https://youtu.be/wyWb4eTK7N8)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# Claude Code /loop Companion Scripts

This repository provides Python scripts that complement the Claude Code /loop command video. These scripts implement the monitoring tasks demonstrated, such as health checks, log monitoring, deploy status checks, and more. You can run these scripts manually or integrate them into your own automation loops (e.g., using cron or Claude Code /loop).

## Files Overview

- `health_check.py`: Checks the health of an API endpoint by making a GET request and verifying the status code.
- `log_monitor.py`: Monitors the last N lines of a log file for error patterns.
- `deploy_monitor.py`: Checks the status of the latest GitHub Actions run for a repository.
- `requirements.txt`: Lists the required Python packages.

## Setup

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd claude-loop-companion
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - For `deploy_monitor.py`, set `GITHUB_TOKEN` to your GitHub personal access token (with repo permissions), `GITHUB_OWNER` to your GitHub username, and `GITHUB_REPO` to your repository name.
   - For `health_check.py`, optionally set `HEALTH_URL` to the API endpoint (defaults to 'https://api.example.com/health').
   - For `log_monitor.py`, set `LOG_FILE` to the path of your log file (defaults to 'log.log').

   Example:
   ```bash
   export GITHUB_TOKEN=your_github_token
   export GITHUB_OWNER=your_github_username
   export GITHUB_REPO=your_repo_name
   export HEALTH_URL=https://your-api.com/health
   export LOG_FILE=log.log
   ```

## Usage

Run each script individually:

- Health check: `python health_check.py`
- Log monitor: `python log_monitor.py`
- Deploy monitor: `python deploy_monitor.py`

To simulate /loop behavior, use cron for scheduling. For example, to run health check every 10 minutes:

```bash
crontab -e
*/10 * * * * cd /path/to/your/repo && python health_check.py
```

These scripts are designed to be simple and can be adapted for use with Claude Code /loop by incorporating their logic into prompts.

## Notes

- Ensure you have permissions to access log files and APIs.
- Error handling is included to prevent crashes.
- For production use, consider adding notifications (e.g., via email or Slack).


---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
