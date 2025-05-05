"""
Run basic sanity checks and unit tests before executing the app.
"""
import subprocess

def run_preflight():
    print("Running preflight checks...")
    result = subprocess.run(["python3", "-m", "unittest", "utils/test_enhancements.py"])
    if result.returncode != 0:
        print("❌ Preflight tests failed. Fix errors before continuing.")
        exit(1)
    print("✅ Preflight checks passed.")

if __name__ == '__main__':
    run_preflight()
