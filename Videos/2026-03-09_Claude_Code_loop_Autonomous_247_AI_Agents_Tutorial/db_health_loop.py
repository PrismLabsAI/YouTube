import os
import time
from sqlalchemy import create_engine, text
from anthropic import Anthropic

# Load environment variables
[REDACTED]
DB_CONNECTION_STRING = os.environ.get('DB_CONNECTION_STRING')

if not all([ANTHROPIC_API_KEY, DB_CONNECTION_STRING]):
    raise ValueError('Missing required environment variables: ANTHROPIC_API_KEY, DB_CONNECTION_STRING')

client = Anthropic(api_key=ANTHROPIC_API_KEY)
engine = create_engine(DB_CONNECTION_STRING)

INTERVAL_HOURS = 1

# Function to check table growth (simplified for demo; assumes a table 'users' with size tracking)
def check_table_growth():
    try:
        with engine.connect() as conn:
            # This is a placeholder; in real DB, query actual sizes
            result = conn.execute(text("SELECT COUNT(*) FROM users"))
            current_size = result.fetchone()[0]
            # Assume previous size is stored or hardcoded for demo
            previous_size = 100000  # Example
            growth_percent = ((current_size - previous_size) / previous_size) * 100
            if growth_percent > 10:
                prompt = f"Table 'users' grew {growth_percent:.2f}% today (from {previous_size} to {current_size}). Alert and suggest investigation."
                message = client.messages.create(
                    model='claude-3-haiku-20240307',
                    max_tokens=100,
                    messages=[{'role': 'user', 'content': prompt}]
                )
                alert = message.content[0].text
                print(f'[Loop Run] Alert: {alert}')
            else:
                print(f'[Loop Run] Table growth: {growth_percent:.2f}%')
    except Exception as e:
        print(f'Error checking DB health: {e}')

# Main loop
print('Starting DB health monitoring loop. Press Ctrl+C to stop.')
while True:
    check_table_growth()
    time.sleep(INTERVAL_HOURS * 3600)