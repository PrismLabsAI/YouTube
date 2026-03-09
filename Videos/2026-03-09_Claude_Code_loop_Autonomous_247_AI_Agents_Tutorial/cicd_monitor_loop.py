import os
import time
import requests
from anthropic import Anthropic

# Load environment variables
[REDACTED]
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_REPO = os.environ.get('GITHUB_REPO')

if not all([ANTHROPIC_API_KEY, GITHUB_TOKEN, GITHUB_REPO]):
    raise ValueError('Missing required environment variables: ANTHROPIC_API_KEY, GITHUB_TOKEN, GITHUB_REPO')

client = Anthropic(api_key=ANTHROPIC_API_KEY)

INTERVAL_MINUTES = 5

# Function to check latest GitHub Actions run
def check_github_actions():
    url = f'https://api.github.com/repos/{GITHUB_REPO}/actions/runs?per_page=1'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        runs = response.json()['workflow_runs']
        if runs:
            latest = runs[0]
            status = latest['conclusion']
            if status == 'failure':
                # Use Claude to analyze and alert
                prompt = f"The latest GitHub Actions run failed. Details: {latest}. Alert the user."
                message = client.messages.create(
                    model='claude-3-haiku-20240307',
                    max_tokens=100,
                    messages=[{'role': 'user', 'content': prompt}]
                )
                alert = message.content[0].text
                print(f'[Loop Run] Alert: {alert}')
            else:
                print(f'[Loop Run] Latest run status: {status}')
        else:
            print('[Loop Run] No runs found.')
    except Exception as e:
        print(f'Error checking GitHub Actions: {e}')

# Main loop
print('Starting CI/CD monitoring loop. Press Ctrl+C to stop.')
while True:
    check_github_actions()
    time.sleep(INTERVAL_MINUTES * 60)