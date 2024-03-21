# scripts/backup_data.py

import shutil
import os

def backup_data():
    source_dir = '/path/to/source/directory'
    destination_dir = '/path/to/destination/directory'
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return
    
    # Create destination directory if it does not exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print("Destination directory created.")
    
    # Copy data from source to destination
    try:
        shutil.copytree(source_dir, destination_dir)
        print("Data backed up successfully.")
    except Exception as e:
        print(f"Error occurred while backing up data: {e}")

# Call the function to execute the backup
backup_data()
