import os
import json
import time
from anthropic import Anthropic

# Initialize Anthropic client with API key from environment variable
client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

# Initial state for the agent
state = {'last_price': None, 'alerts': []}

# Load existing state if available
try:
    with open('state.json', 'r') as f:
        state = json.load(f)
except FileNotFoundError:
    pass  # No existing state, start fresh

while True:
    try:
        # Simulate fetching BTC price (replace with real API like CoinGecko)
        btc_price = 95000  # Simulated value; in real use, fetch from API
        
        # Check condition for alert
        if btc_price > 100000:
            alert_msg = f'Alert: BTC > 100k at {btc_price}'
            state['alerts'].append(alert_msg)
            print(alert_msg)
        
        # Update state
        state['last_price'] = btc_price
        
        # Save state to file
        with open('state.json', 'w') as f:
            json.dump(state, f)
        
        print(f'Iteration: BTC price {btc_price}, state saved')
        
        # Sleep for 5 minutes (300 seconds)
        time.sleep(300)
    
    except Exception as e:
        print(f'Error in loop: {e}')
        time.sleep(60)  # Retry after 1 minute on error