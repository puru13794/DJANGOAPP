import subprocess

# Run Django migrations
subprocess.run(["python3.10", "manage.py", "migrate"])