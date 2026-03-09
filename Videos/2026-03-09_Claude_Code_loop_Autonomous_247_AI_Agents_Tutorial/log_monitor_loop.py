import os
import time
from anthropic import Anthropic

# Load environment variables
[REDACTED]
LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH')

if not all([ANTHROPIC_API_KEY, LOG_FILE_PATH]):
    raise ValueError('Missing required environment variables: ANTHROPIC_API_KEY, LOG_FILE_PATH')

client = Anthropic(api_key=ANTHROPIC_API_KEY)

INTERVAL_MINUTES = 15

# Function to analyze logs
def analyze_logs():
    try:
        with open(LOG_FILE_PATH, 'r') as f:
            lines = f.readlines()[-100:]  # Last 100 lines
        log_content = ''.join(lines)
        # Use Claude to summarize errors/warnings
        prompt = f"Summarize errors and warnings from these log lines: {log_content}"
        message = client.messages.create(
            model='claude-3-haiku-20240307',
            max_tokens=200,
            messages=[{'role': 'user', 'content': prompt}]
        )
        summary = message.content[0].text
        print(f'[Loop Run] Log Summary: {summary}')
    except Exception as e:
        print(f'Error analyzing logs: {e}')

# Main loop
print('Starting log monitoring loop. Press Ctrl+C to stop.')
while True:
    analyze_logs()
    time.sleep(INTERVAL_MINUTES * 60)