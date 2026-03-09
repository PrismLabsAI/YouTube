# WPScan 2026: Kali CVE Scan Tutorial

> **[Watch on YouTube](https://youtu.be/TZgT9MQxQ80)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# WPScan Companion Scripts for Kali Linux

This repository provides companion scripts and examples to complement the WPScan tutorial video by Prism Labs AI. These are designed for penetration testers using Kali Linux to scan WordPress sites for vulnerabilities.

## Files Overview

- `README.md`: This file, explaining setup and usage.
- `basic_scan.sh`: Bash script for basic enumeration scan.
- `aggressive_scan.sh`: Bash script for aggressive CVE hunting scan.
- `parse_output.py`: Python script to parse WPScan JSON output and summarize vulnerabilities.
- `requirements.txt`: Python dependencies for `parse_output.py`.
- `custom_wordlist.txt`: Example custom wordlist for brute-forcing usernames or plugins.

## Setup

1. Ensure you have Kali Linux installed.
2. Install Ruby and WPScan as shown in the video:
   ```bash
   sudo apt update && sudo apt install ruby ruby-dev -y
   gem install wpscan
   ```
3. Obtain a WPScan API token from https://wpscan.com/api and set it as an environment variable:
   ```bash
   export WP_API_TOKEN=your_api_token_here
   ```
4. Update WPScan database:
   ```bash
   wpscan --update
   ```
5. For the Python script, install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Scan
Run `basic_scan.sh` to perform a basic enumeration scan on a target URL.

```bash
chmod +x basic_scan.sh
./basic_scan.sh https://example-wordpress-site.com
```

This will enumerate vulnerable plugins and themes, saving output to `basic_scan_output.txt`.

### Aggressive Scan
Run `aggressive_scan.sh` for deep CVE hunting.

```bash
chmod +x aggressive_scan.sh
./aggressive_scan.sh https://example-wordpress-site.com
```

This uses aggressive detection mode and saves output to `aggressive_scan_output.json`.

### Parse Output
After running a scan that outputs JSON (e.g., aggressive scan), use `parse_output.py` to summarize vulnerabilities.

```bash
python parse_output.py aggressive_scan_output.json
```

It will print a summary of found vulnerabilities.

### Custom Wordlist
Use `custom_wordlist.txt` with WPScan's `--wordlist` option for custom brute-forcing.

## Notes

- Replace `https://example-wordpress-site.com` with your actual target URL.
- Ensure you have permission to scan the target (ethical hacking only).
- API token is required for detailed vulnerability info.
- Scripts include error handling and comments for beginners.

For more details, watch the full video: https://youtu.be/TZgT9MQxQ80

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
