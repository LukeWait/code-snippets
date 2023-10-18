'''
Description: a Python script that backs up specified files or directories to a designated backup location.
1) Fix the file.
2) Then see if we can make it zip a file/folder
'''

import shutil
import os
import tkinter as tk
from tkinter import filedialog

def backup_files(source_dir, backup_dir):
    try:
        # Create a full path for the backup directory
        backup_path = os.path.join(backup_dir, f"{os.path.basename(source_dir)}-copy")
        
        shutil.copytree(source_dir, backup_path) # Copy the source directory to the backup directory
        print(f"Backup successful! Files copied to: {backup_path}")
    except shutil.Error as e:
        print(f"Error: {e}")

def zip_files(source_dir, zip_dir):
    try:
        # Create a full path for the zip file
        zip_path = os.path.join(zip_dir, f"{os.path.basename(source_dir)}")
        
        shutil.make_archive(zip_path, 'zip', source_dir) # Create a zip archive of the source directory
        print(f"Zip file {zip_path}.zip created successfully!")
    except shutil.Error as e:
        print(f"Error: {e}")
        
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

source_directory = filedialog.askdirectory(title="Select the source directory")
if not source_directory:
    print("No source directory selected. Exiting.")
    exit(1)

backup_directory = filedialog.askdirectory(title=f"Select the backup directory for '{os.path.basename(source_directory)}'")
zip_directory = filedialog.askdirectory(title=f"Select the zip directory for '{os.path.basename(source_directory)}")

if not backup_directory or not zip_directory:
    print("No backup or zip directory selected. Exiting.")
    exit(1)

backup_files(source_directory, backup_directory)
zip_files(source_directory, zip_directory)

