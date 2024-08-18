"""
My attempt on exercise for finding phone number present in one file among large number of text files
"""

import os
import re

# pwd is the directory in which current file is present
files_directory_path = '../Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/extracted_content'
pattern = r'(\d{3})-(\d{3})-(\d{4})'

for folder, sub_folders, files in os.walk(files_directory_path):
    # print(f"checking in folder {folder}")
    for filename in files:
        myfile = open(os.path.join(folder,filename), "r")
        content = myfile.read()
        # print(f"checking in file {filename}")
        match = re.search(pattern, content)
        if match:
            print(f"match = {match}")
            print(f"phone number {match.group(0)} found in file {filename} in folder {folder}")
