# log_monitor.py
# Script to monitor the last 50 lines of a log file for errors.
# Usage: python log_monitor.py
# Set LOG_FILE environment variable for custom log path.

import os
import re

def monitor_logs():
    log_file = os.environ.get('LOG_FILE', 'log.log')
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()[-50:]  # Last 50 lines
        error_pattern = re.compile(r'ERROR|error|Exception', re.IGNORECASE)
        errors = [line.strip() for line in lines if error_pattern.search(line)]
        if errors:
            print("Errors found in the last 50 lines:")
            for error in errors:
                print(error)
        else:
            print("No errors found in the last 50 lines.")
    except FileNotFoundError:
        print(f"Log file not found: {log_file}")
    except Exception as e:
        print(f"Error monitoring logs: {e}")

if __name__ == "__main__":
    monitor_logs()
