# Sample buggy Python code for demonstration
# This file contains intentional bugs: security, performance, style

def authenticate(user):
    # Bug: No null check for user.id - security vulnerability
    if not user:
        raise ValueError("Unauthorized")
    return True

def process_file(file_path):
    # Bug: File not closed - performance leak
    f = open(file_path, 'r')
    data = f.read()
    return data

def calculate_sum(a, b):
    # Bug: Style - inconsistent naming, no docstring
    result = a + b
    return result

# Usage
user = None  # Simulate null user
authenticate(user)
data = process_file('test.txt')
sum_val = calculate_sum(1, 2)