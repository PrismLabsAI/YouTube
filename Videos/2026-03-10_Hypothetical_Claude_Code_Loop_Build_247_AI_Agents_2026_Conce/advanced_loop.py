import yaml
import json
import time
import os
from anthropic import Anthropic

# Load configuration from YAML
with open('advanced_loop.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

# Initial state
state = {'retries': 0}

# Load existing state if available
try:
    with open(config['state']['file'], 'r') as f:
        state = json.load(f)
except FileNotFoundError:
    pass

while True:
    try:
        # Simulate actions: fetch, analyze, act using Claude
        response = client.messages.create(
            model='claude-3-haiku-20240307',
            max_tokens=100,
            messages=[{'role': 'user', 'content': 'Analyze data and perform action based on config.'}]
        )
        print('Action executed successfully')
        state['retries'] = 0  # Reset retries on success
    
    except Exception as e:
        state['retries'] += 1
        if state['retries'] < config['recovery']['max_retries']:
            backoff_time = 2 ** state['retries']  # Exponential backoff
            print(f'Retry {state["retries"]} after {backoff_time}s: {e}')
            time.sleep(backoff_time)
            continue
        else:
            print(f'Max retries reached. Error: {e}')
            break  # Or handle differently
    
    # Save state
    with open(config['state']['file'], 'w') as f:
        json.dump(state, f)
    
    # Sleep based on trigger interval
    time.sleep(config['trigger']['interval'])