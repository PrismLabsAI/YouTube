# Claude Code /loop: Autonomous 24/7 AI Agents Tutorial

> **[Watch on YouTube](https://youtu.be/rApuKStTLsM)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# Autonomous AI Agents with Claude API

This repository provides Python scripts that simulate the autonomous loop functionality described in the YouTube video "Claude Code /loop: Autonomous 24/7 AI Agents Tutorial" by Prism Labs AI. Since the `/loop` command in Claude Code is conceptual, these scripts use the Anthropic Claude API to create real, working autonomous agents for monitoring tasks.

## Features

- **CI/CD Monitoring**: Checks GitHub Actions runs and alerts on failures using Claude for analysis.
- **Log Monitoring**: Analyzes server logs for errors and warnings, summarized by Claude.
- **Database Health Checks**: Monitors database table growth and alerts if thresholds are exceeded.
- **Loop Management**: A manager script to start, stop, and list loops using APScheduler.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <this-repo-url>
   cd autonomous-agents
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key (get from https://console.anthropic.com/).
   - `GITHUB_TOKEN`: Your GitHub personal access token (for CI/CD monitoring).
   - `GITHUB_REPO`: Your GitHub repo in format `owner/repo` (e.g., `myuser/myrepo`).
   - `LOG_FILE_PATH`: Path to your server log file (e.g., `/path/to/your/log/file`).
   - `DB_CONNECTION_STRING`: Database connection string (e.g., for SQLite: `sqlite:///your_db.db`; for PostgreSQL: `postgresql://user:password@host/db`).

   Example:
   ```bash
   export [REDACTED]
   export GITHUB_TOKEN='your-github-token'
   export GITHUB_REPO='myuser/myrepo'
   export LOG_FILE_PATH='/path/to/your/log/file'
   export DB_CONNECTION_STRING='sqlite:///your_db.db'
   ```

## Usage

### Running Individual Loops

Each loop script runs indefinitely, checking at the specified interval. Run them in the background using `nohup` or a process manager like `systemd` for 24/7 operation.

- **CI/CD Monitor** (every 5 minutes):
  ```bash
  python cicd_monitor_loop.py
  ```

- **Log Monitor** (every 15 minutes):
  ```bash
  python log_monitor_loop.py
  ```

- **DB Health Monitor** (every 1 hour):
  ```bash
  python db_health_loop.py
  ```

### Using the Loop Manager

The manager uses APScheduler to run jobs in the same process. It's for demo purposes; for production, use cron or similar.

```bash
python loop_manager.py
```

Inside the script, you can start/stop loops by modifying the code (see comments).

## Files

- `requirements.txt`: Python dependencies.
- `cicd_monitor_loop.py`: Script for CI/CD monitoring loop.
- `log_monitor_loop.py`: Script for log monitoring loop.
- `db_health_loop.py`: Script for database health loop.
- `loop_manager.py`: Scheduler-based loop manager.

## Notes

- These scripts use real APIs and require valid keys.
- Error handling is included; check logs for issues.
- For production, integrate with cron jobs instead of infinite loops.
- Inspired by the video's conceptual `/loop`; adapt as needed.

## License

MIT License.

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
