import os
import json
from pathlib import Path

def list_files(startpath, max_depth):
    tree = {}
    startpath = str(startpath)  # Convert Path object to string
    for root, dirs, files in os.walk(startpath):
        depth = root[len(startpath) + len(os.path.sep):].count(os.path.sep)
        if depth > max_depth:
            dirs[:] = []  # Don't go deeper than max_depth
        else:
            tree[root] = files
    return tree

def main():
    start_directory = Path.cwd()  # Start from the current directory
    max_depth = 2  # Maximum depth of directory traversal
    
    try:
        file_tree = list_files(start_directory, max_depth)
        with open('file_structure.json', 'w') as file:
            json.dump(file_tree, file, indent=4)
        print("File structure has been saved to 'file_structure.json'.")
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
