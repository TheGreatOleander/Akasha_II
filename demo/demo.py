
import subprocess, time

print("=== Akasha Demonstration ===")
subprocess.call(["python", "akasha.py", "add", "Akasha awakens"])
subprocess.call(["python", "akasha.py", "add", "Memory shapes identity"])
time.sleep(1)
subprocess.call(["python", "akasha.py", "recall", "Akasha"])
time.sleep(1)
subprocess.call(["python", "akasha.py", "recall"])
