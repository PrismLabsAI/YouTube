#!/usr/bin/env python3
"""
Setup script to install dependencies and verify Google Cloud setup.
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages from requirements.txt."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def verify_setup():
    """Verify Google Cloud project and authentication."""
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    if not project_id:
        print("Error: GOOGLE_CLOUD_PROJECT environment variable not set.")
        sys.exit(1)
    print(f"Project ID: {project_id}")
    
    try:
        from google.cloud import aiplatform
        aiplatform.init(project=project_id, location='us-central1')
        print("Google Cloud setup verified.")
    except Exception as e:
        print(f"Error verifying setup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
    verify_setup()
    print("Setup complete. You can now run the example scripts.")