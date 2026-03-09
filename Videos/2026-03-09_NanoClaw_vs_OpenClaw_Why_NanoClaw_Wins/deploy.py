from flask import Flask, request, jsonify
from nanoclaw import NanoClawAgent

app = Flask(__name__)
agent = NanoClawAgent('config.yaml')

@app.route('/run', methods=['POST'])
def run_agent():
    data = request.get_json()
    task = data.get('task', '')
    if not task:
        return jsonify({'error': 'Task required'}), 400
    try:
        result = agent.run_task(task)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return "NanoClaw Agent Service Running. POST to /run with {'task': 'your task here'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)