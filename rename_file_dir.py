import os
import shutil
import re

def rename_files(directory, pattern):
    # Validate directory path
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Compile a regular expression pattern based on the input pattern
    regex_pattern = re.compile(pattern)

    # Rename matching files
    for filename in files:
        if regex_pattern.match(filename):
            # Generate the new name based on the pattern
            new_name = regex_pattern.sub(r'\1', filename)

            # Construct the full file paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            # Rename the file
            shutil.move(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    # Input directory path and pattern
    directory_path = input("Enter the directory path: ")
    renaming_pattern = input("Enter the renaming pattern using regular expression: ")

    # Call the function to rename files
    rename_files(directory_path, renaming_pattern)
