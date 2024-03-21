# scripts/update_dependencies.py

import subprocess

def update_dependencies():
    print("Updating dependencies...")
    try:
        # Use subprocess to run pip command to upgrade all packages
        subprocess.run(["pip", "install", "--upgrade", "pip"])
        subprocess.run(["pip", "install", "--upgrade", "-r", "requirements.txt"])
        print("Dependencies updated successfully.")
    except Exception as e:
        print(f"Failed to update dependencies: {e}")

if __name__ == "__main__":
    update_dependencies()
