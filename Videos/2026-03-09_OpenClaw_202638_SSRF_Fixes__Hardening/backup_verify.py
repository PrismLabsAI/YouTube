# backup_verify.py
# Demonstrates tamper-proof backup and verification using SHA-256 hashing,
# inspired by OpenClaw 2026.3.8 CLI backup/verify feature.

import hashlib
import os
import sys

def compute_hash(file_path):
    """Compute SHA-256 hash of a file."""
    try:
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None

def backup_and_verify(directory, output_file):
    """Simulate backup by hashing files and saving to a 'baseline' file."""
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            h = compute_hash(path)
            if h:
                hashes[path] = h
    
    # Save hashes to baseline file
    with open('baseline.sha256', 'w') as f:
        for path, h in hashes.items():
            f.write(f"{h}  {path}\n")
    
    print(f"Backup simulated. Baseline saved to baseline.sha256.")
    
    # Verify immediately
    verify_hashes('baseline.sha256')

def verify_hashes(baseline_file):
    """Verify files against baseline hashes."""
    try:
        with open(baseline_file, 'r') as f:
            baseline = {}
            for line in f:
                parts = line.strip().split('  ', 1)
                if len(parts) == 2:
                    baseline[parts[1]] = parts[0]
        
        mismatches = 0
        for path, expected in baseline.items():
            actual = compute_hash(path)
            if actual != expected:
                print(f"Mismatch: {path}")
                mismatches += 1
        
        if mismatches == 0:
            print("Verification complete: All files match baseline.")
        else:
            print(f"Verification failed: {mismatches} mismatches.")
    except FileNotFoundError:
        print(f"Error: Baseline file {baseline_file} not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup_verify.py <directory_to_backup>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    backup_and_verify(directory, 'backup.tar.gz')  # Simulate output file
