from nanoclaw import NanoClawAgent
import time

# Benchmark script comparing tasks
def benchmark():
    agent = NanoClawAgent('config.yaml')
    tasks = {
        'Reasoning': 'Solve: 2x + 3 = 7',
        'Coding': 'Write a Python function to reverse a string.',
        'Research': 'What is the capital of France?'
    }
    
    print("Benchmark Results (Average Time in seconds):")
    print("+----------------+--------+")
    print("| Task           | Time   |")
    print("+----------------+--------+")
    
    for task_name, task in tasks.items():
        avg_time = agent.benchmark_task(task)
        print(f"| {task_name:<14} | {avg_time:.2f}   |")
    
    print("+----------------+--------+")

if __name__ == "__main__":
    benchmark()