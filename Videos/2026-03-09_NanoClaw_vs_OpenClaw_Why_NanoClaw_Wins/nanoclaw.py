import os
import openai
import yaml
from typing import Dict, Any

class NanoClawAgent:
    """
    A lightweight AI agent framework for quick task execution.
    """
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.api_key = os.environ.get('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("Please set OPENAI_API_KEY environment variable.")
        self.client = openai.OpenAI(api_key=self.api_key)

    def run_task(self, task: str) -> str:
        """
        Run a task using the configured model and reasoning.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.config.get('model', 'gpt-3.5-turbo'),
                messages=[{"role": "user", "content": task}],
                max_tokens=1000
            )
            return response.choices[0].message.content.strip()
        except openai.OpenAIError as e:
            return f"Error: {str(e)}"

    def benchmark_task(self, task: str, iterations: int = 5) -> float:
        """
        Benchmark task execution time.
        """
        import time
        times = []
        for _ in range(iterations):
            start = time.time()
            self.run_task(task)
            end = time.time()
            times.append(end - start)
        return sum(times) / len(times)

# Example usage (can be run standalone for testing)
if __name__ == "__main__":
    agent = NanoClawAgent('config.yaml')
    result = agent.run_task("Analyze the top 5 trending GitHub repos.")
    print(result)