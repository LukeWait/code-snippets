'''
Description: a Python script that backs up specified files or directories to a designated backup location.
'''

import shutil
import os
import tkinter as tk # GUI editor
from tkinter import filedialog # Allows users to interact with the file system using tkinter


def backup_files(source_dir, backup_dir):
    try:
        # Create a full path for the backup directory
        backup_path = os.path.join(backup_dir, f"{os.path.basename(source_dir)}-copy")
        # Copy the source directory to the backup directory
        shutil.copytree(source_dir, backup_path)
        print(f"Backup successful! Files copied to: {backup_path}")
    except shutil.Error as e:
        print(f"Error: {e}")

def zip_files(source_dir, zip_dir):
    try:
        # Create a full path for the zip file
        zip_path = os.path.join(zip_dir, f"{os.path.basename(source_dir)}")
        # Create a zip archive of the source directory
        shutil.make_archive(zip_path, 'zip', source_dir)
        print(f"Zip file {zip_path}.zip created successfully!")
    except shutil.Error as e:
        print(f"Error: {e}")


root = tk.Tk() # Create an instance of tkinter
root.withdraw() # Hides the main tkinter window as we are only using the filedialog module

# Brings up a window for navigating to source folder
source_directory = filedialog.askdirectory(title="Select the source directory")
# If user exits the window, it will terminate the script early
if not source_directory:
    print("No source directory selected. Exiting.")
    exit(1)

# Brings up a windows for navigating to backup and zip directory
backup_directory = filedialog.askdirectory(title=f"Select the backup directory")
zip_directory = filedialog.askdirectory(title=f"Select the zip directory")
# If a directory was provided it will call the appropriate function(s)
if backup_directory:
    backup_files(source_directory, backup_directory)
if zip_directory:
    zip_files(source_directory, zip_directory)
# If neither directory was provided, it will exit
if not backup_directory and not zip_directory:
    print("No backup or zip directory selected. Exiting.")
    exit(1)

