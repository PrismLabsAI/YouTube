import requests
from nanoclaw import NanoClawAgent

# Example: Web-scraping and reasoning agent
def main():
    agent = NanoClawAgent('config.yaml')
    
    # Simulate web search (using GitHub API for trending repos)
    try:
        response = requests.get('https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc&per_page=5')
        response.raise_for_status()
        repos = response.json()['items']
        repo_names = [repo['full_name'] for repo in repos]
        
        # Use agent for analysis
        task = f"Analyze these trending GitHub repos: {', '.join(repo_names)}. Summarize their purposes."
        result = agent.run_task(task)
        print("Agent Analysis:")
        print(result)
    except requests.RequestException as e:
        print(f"Error fetching repos: {e}")
    except Exception as e:
        print(f"Agent error: {e}")

if __name__ == "__main__":
    main()