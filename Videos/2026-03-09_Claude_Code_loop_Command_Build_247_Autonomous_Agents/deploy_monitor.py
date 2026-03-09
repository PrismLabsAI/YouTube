# deploy_monitor.py
# Script to check the status of the latest GitHub Actions run.
# Usage: python deploy_monitor.py
# Set GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPO environment variables.

import os
import requests

def check_deploy():
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN not set.")
        return
    
    owner = os.environ.get('GITHUB_OWNER')
    if not owner:
        print("Error: GITHUB_OWNER not set.")
        return
    
    repo = os.environ.get('GITHUB_REPO')
    if not repo:
        print("Error: GITHUB_REPO not set.")
        return
    
    url = f'https://api.github.com/repos/{owner}/{repo}/actions/runs?per_page=1'
    headers = {'Authorization': f'token {token}'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data['workflow_runs']:
                run = data['workflow_runs'][0]
                status = run['status']
                conclusion = run['conclusion']
                print(f"Run #{run['run_number']}: Status {status.upper()} ({conclusion or 'in progress'}).")
                if conclusion == 'failure':
                    print("Alert: Deploy failed!")
                else:
                    print("No issues detected.")
            else:
                print("No runs found.")
        else:
            print(f"Error fetching runs: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error checking deploy: {e}")

if __name__ == "__main__":
    check_deploy()
