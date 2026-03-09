import os
import anthropic
import re
import json
from collections import deque
import traceback
import time

# Load Anthropic API key from environment variable
API_KEY = os.environ.get('ANTHROPIC_API_KEY')
if not API_KEY:
    raise ValueError('ANTHROPIC_API_KEY environment variable not set')

client = anthropic.Anthropic(api_key=API_KEY)

# Safe execution environment (limited builtins for security)
SAFE_GLOBALS = {
    '__builtins__': {
        'print': print,
        'len': len,
        'range': range,
        'int': int,
        'str': str,
        'list': list,
        'dict': dict,
        'sum': sum,
        'max': max,
        'min': min,
        # Add more as needed, but keep it minimal
    }
}

def execute_code(code):
    """Execute code safely with error handling."""
    try:
        exec(code, SAFE_GLOBALS)
        return 'Execution successful'
    except Exception as e:
        error_msg = f'Execution error: {e}\n{traceback.format_exc()}'
        print(error_msg)
        return error_msg

def load_state():
    """Load state from JSON file."""
    try:
        with open('state.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'tasks': deque(), 'logs': [], 'metrics': {'iterations': 0, 'errors': 0}}

def save_state(state):
    """Save state to JSON file."""
    with open('state.json', 'w') as f:
        json.dump(state, f, indent=2)

def main():
    state = load_state()
    # Add initial task if none
    if not state['tasks']:
        state['tasks'].append('Build a simple counter app')
    
    while True:
        task = state['tasks'].popleft() if state['tasks'] else 'Self-improve: Optimize code execution'
        last_log = state['logs'][-1] if state['logs'] else 'None'
        
        prompt = f"""Task: {task}
Review last output: {last_log}
If there was an error, fix it. Generate Python code to complete the task. Output only the code in a ```python code block.
"""
        
        try:
            response = client.messages.create(
                model='claude-3-5-sonnet-20240620',
                max_tokens=1000,
                messages=[{'role': 'user', 'content': prompt}]
            )
            content = response.content[0].text
            code_match = re.search(r'```python\n(.*?)\n```', content, re.DOTALL)
            if code_match:
                code = code_match.group(1)
                result = execute_code(code)
                state['logs'].append(f'Task: {task} - {result}')
                state['metrics']['iterations'] += 1
                # Simulate self-improvement: if errors > threshold, add self-improve task
                if 'error' in result.lower():
                    state['metrics']['errors'] += 1
                    if state['metrics']['errors'] > 2:
                        state['tasks'].append('Self-improve: Add better error handling')
            else:
                state['logs'].append(f'Task: {task} - No code generated')
        except Exception as e:
            state['logs'].append(f'Task: {task} - API error: {e}')
        
        save_state(state)
        time.sleep(1)  # Brief pause to avoid rate limits
        
        # For demo, break after 5 iterations
        if state['metrics']['iterations'] >= 5:
            break

if __name__ == '__main__':
    main()