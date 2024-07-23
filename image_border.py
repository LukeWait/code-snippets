# -*- coding: utf-8 -*-
"""
Project: Add Border to Image Script
Description: Allows users to choose an image with a file explorer, add a border to it,
             and save the modified image to a specified location.
Version: 1.2.0
Author: ┬  ┬ ┬┬┌─┌─┐┬ ┬┌─┐╦╔╦╗
        │  │ │├┴┐├┤ │││├─┤║ ║
        ┴─┘└─┘┴ ┴└─┘└┴┘┴ ┴╩ ╩
Date: July 23, 2024
License: MIT License

Dependencies:
customtkinter==5.2.1
Pillow==10.1.0

GitHub Repository: https://github.com/LukeWait/code-snippets
"""

import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageOps
import os
import subprocess
import sys


class BorderSettingsUI(ctk.CTk):
    """Provides graphical user interface to choose border settings.
    
    Utilizes the customtkinter library (ctk) for appearance settings and interactions.

    Attributes:
        root (CTk): The main window of the application.
        border_size (int): The size of the border to be added.
        border_color (str): The color of the border in hexadecimal format.
        border_size_field (CTkEntry): Entry field for the border size.
        border_color_field (CTkEntry): Entry field for the border color.
        status_label (CTkLabel): Label to display status messages.

    Methods:
        __init__(): Initializes the user interface.
        on_ok(): Handles the OK button click event.
        on_cancel(): Handles the Cancel button click event and exits the program.
        get_border_settings(): Returns the border settings entered by the user.
    """
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")
        self.title("Border Settings")
        self.geometry("300x180")
        self.grid_rowconfigure((2), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.border_size = 1
        self.border_color = "#4a4a4a"

        # Border size entry
        ctk.CTkLabel(self, text="Border size:").grid(row=0, column=0, padx=10, pady=(20, 5), sticky='e')
        self.border_size_field = ctk.CTkEntry(self, placeholder_text=self.border_size, width=140)
        self.border_size_field.grid(row=0, column=1, padx=10, pady=(20, 5), sticky='ew')
        self.border_size_field.bind("<Return>", lambda event: self.on_ok())

        # Border color entry
        ctk.CTkLabel(self, text="Border color:").grid(row=1, column=0, padx=10, pady=(5, 10), sticky='e')
        self.border_color_field = ctk.CTkEntry(self, placeholder_text=self.border_color, width=140)
        self.border_color_field.grid(row=1, column=1, padx=10, pady=(5, 10), sticky='ew')
        self.border_color_field.bind("<Return>", lambda event: self.on_ok())

        # Buttons
        ctk.CTkButton(self, text="OK", command=self.on_ok).grid(row=2, column=1, padx=10, pady=10)
        ctk.CTkButton(self, text="Cancel", command=self.on_cancel).grid(row=2, column=0, padx=10, pady=10)
        
        # Status message
        self.status_label = ctk.CTkLabel(self, text="", text_color="red")
        self.status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 5))

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)
        self.mainloop()

    def on_ok(self):
        """Handles OK button click.
        """
        input_border_size = self.border_size_field.get().strip()
        input_border_color = self.border_color_field.get().strip()

        try:
            if input_border_size:
                self.border_size = int(input_border_size)

            if input_border_color:
                if not (input_border_color.startswith('#') and len(input_border_color) == 7):
                    raise ValueError("Invalid color format")
                self.border_color = input_border_color

        except ValueError as e:
            self.status_label.configure(text=f"Error: {e}")
            return

        self.destroy()

    def on_cancel(self):
        """Handles Cancel button click and exits the program.
        """
        print("Window closed by user. Exiting.")
        self.destroy()
        exit(1)

    def get_border_settings(self):
        """Returns the border settings.
        """
        return self.border_size, self.border_color


def add_border(input_image_path, output_image_path, border_size, color):
    """Adds a border to the specified image and saves it to the given path.

    Args:
        input_image_path (str): The file path of the input image.
        output_image_path (str): The file path where the image with the border will be saved.
        border_size (int): The size of the border to add.
        color (str): The color of the border in hexadecimal format (e.g., "#FF0000").

    Raises:
        IOError: If there's an issue opening or saving the image.
    """
    try:
        img = Image.open(input_image_path)
        img_with_border = ImageOps.expand(img, border=border_size, fill=color)
        img_with_border.save(output_image_path)
        
    except IOError as e:
        print(f"Error processing image: {e}")
        exit(1)


def open_file_explorer(file_path):
    """Opens the file explorer at the specified file path.

    Args:
        file_path (str): The file path to open in the file explorer.

    Raises:
        Exception: If there's an unexpected error when opening the file explorer.
    """
    abs_path = os.path.abspath(file_path)
    
    try:
        # For Windows
        if os.name == 'nt':
            subprocess.Popen(f'explorer /select,"{abs_path}"', shell=True)
        # For macOS
        elif sys.platform == 'darwin':
            subprocess.run(['open', '-R', abs_path], check=True)
        # For Linux
        elif os.name == 'posix':
            output_dir = os.path.dirname(abs_path)
            subprocess.run(['xdg-open', output_dir], check=True)    
            
    except subprocess.CalledProcessError as e:
        print(f"Error opening file explorer: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Open file dialog to select the input image file
input_image_path = filedialog.askopenfilename(title="Select the input image file")
if not input_image_path:
    print("No input image selected. Exiting.")
    exit(1)

# Open file dialog to select the output file path
output_image_path = filedialog.asksaveasfilename(title="Select the output file path")
if not output_image_path:
    print("No output file path selected. Exiting.")
    exit(1)

# Get border settings from the user
ui = BorderSettingsUI()
border_size, color = ui.get_border_settings()

# Add border to the selected image and save it to the chosen location
add_border(input_image_path, output_image_path, border_size, color)

# Open file explorer at the new file
open_file_explorer(output_image_path)
