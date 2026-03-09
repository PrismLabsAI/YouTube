# WPScan Mastery: WordPress CVE Scanning 2024

> **[Watch on YouTube](https://youtu.be/Lhulv9oaAMY)**

Published by [Prism Labs AI](https://youtube.com/@prismlabsai)

---

# WPScan Mastery Companion Code

This repository provides companion code for the YouTube video 'WPScan Mastery: WordPress CVE Scanning 2024' by Prism Labs AI. It includes scripts to automate WPScan usage, parse results, and filter CVEs for penetration testing workflows.

## Files Overview

- **README.md**: This file – setup and usage instructions.
- **requirements.txt**: Python dependencies for the scripts.
- **wpscan_automate.py**: Python script to run WPScan scans and parse JSON output.
- **run_wpscan.sh**: Bash script for quick WPScan execution with common options.
- **parse_cves.py**: Python script to filter and report high-severity CVEs from WPScan output.

## Setup

1. **Install WPScan**: Follow the video's installation guide. On Kali Linux: `sudo apt update && sudo apt install wpscan -y`.
2. **Get API Token**: Sign up at [wpscan.com](https://wpscan.com) for a free API token to unlock full features.
3. **Clone this repo**: `git clone <repo-url>`.
4. **Install Python dependencies**: `pip install -r requirements.txt`.
5. **Set Environment Variable**: Export your API token: `export WPSCAN_API_TOKEN=your_token_here`.

## Usage

### Running a Basic Scan with Bash Script

```bash
./run_wpscan.sh https://target.example.com
```

This runs a basic enumeration scan. Modify the script for advanced options.

### Automating Scans with Python

```python
python wpscan_automate.py --url https://target.example.com --output results.json
```

This script calls WPScan, saves output to JSON, and prints a summary.

### Filtering CVEs

After running a scan, parse results:

```python
python parse_cves.py results.json
```

It filters for CVSS scores >= 7.0 and prints critical findings.

## Notes

- All scripts include error handling and are beginner-friendly.
- Use on your own controlled environments only; ethical hacking rules apply.
- For full WPScan features, ensure your API token is set.
- Scripts use subprocess to call WPScan, assuming it's installed.

For more details, watch the video: [https://youtu.be/Lhulv9oaAMY](https://youtu.be/Lhulv9oaAMY).

---

## Disclaimer

This code is provided as-is for educational purposes only. **Use at your own risk** — no warranty is provided, express or implied. The authors are not responsible for any damages or issues arising from the use of this code.

## License

MIT License

---

*Made by [Prism Labs AI](https://youtube.com/@prismlabsai)*
