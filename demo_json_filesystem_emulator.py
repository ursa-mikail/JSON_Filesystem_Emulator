## create a json file
import json

# Sample filesystem represented as a nested dictionary (JSON structure)
filesystem = {
    "root": {
        "folder1": {
            "subfolder1": {},
            "subfolder2": {
                "file1.txt": "This is file1 content",
                "file2.txt": "This is file2 content"
            },
            "file3.txt": "This is file3 content"
        },
        "folder2": {
            "subfolder3": {
                "file4.txt": "This is file4 content"
            }
        }
    }
}

json_file = "filesystem.json"

# Save the structure as a JSON file
with open(json_file, 'w') as f:
    json.dump(filesystem, f, indent=4)

## List json file structure
import json

# Load the filesystem JSON from a file
def load_filesystem(path="filesystem.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {path} not found")
        return {}

# List the contents of a "directory" in the JSON filesystem
def list_dir(filesystem, path):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                print(f"Error: '{path}' not found in filesystem")
                return
        if isinstance(current_dir, dict):
            print(f"Contents of '{path}': {list(current_dir.keys())}")
        else:
            print(f"'{path}' is not a directory")
    except Exception as e:
        print(f"Error listing directory contents: {e}")

# Walk through the "directory" structure and print subfolders and files
def walk_dir(filesystem, path):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                print(f"Error: '{path}' not found in filesystem")
                return
        if isinstance(current_dir, dict):
            for dir_name, content in current_dir.items():
                print(f"Root: {path}/{dir_name}")
                if isinstance(content, dict):
                    print(f"Subfolders: {list(content.keys())}")
                else:
                    print(f"File: {dir_name}")
                print()
        else:
            print(f"'{path}' is not a directory")
    except Exception as e:
        print(f"Error walking directory: {e}")

# Get detailed file or folder info (like size, type, timestamps)
def get_file_info(filesystem, path):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                raise ValueError(f"'{path}' not found in filesystem")
        
        if isinstance(current_dir, dict):
            return {
                "path": path,
                "type": "Directory",
                "contents": list(current_dir.keys())
            }
        else:
            return {
                "path": path,
                "type": "File",
                "size": len(current_dir),
                "content": current_dir
            }
    except Exception as e:
        print(f"Error getting file info: {e}")
        return {}

# Pretty print the JSON structure
def pretty_print_json(data):
    print(json.dumps(data, indent=4))

# Demonstrating use
filesystem = load_filesystem()

# Listing contents of 'root/folder1'
list_dir(filesystem, "root/folder1")

# Walking through the 'root/folder1'
walk_dir(filesystem, "root/folder1")

# Getting file information
file_info = get_file_info(filesystem, "root/folder1/file3.txt")
pretty_print_json(file_info)

# Listing contents 
list_dir(filesystem, "root/")
list_dir(filesystem, "root/folder1/subfolder2")

pretty_print_json(filesystem)

"""
Contents of 'root/folder1': ['subfolder1', 'subfolder2', 'file3.txt']
Root: root/folder1/subfolder1
Subfolders: []

Root: root/folder1/subfolder2
Subfolders: ['file1.txt', 'file2.txt']

Root: root/folder1/file3.txt
File: file3.txt

{
    "path": "root/folder1/file3.txt",
    "type": "File",
    "size": 21,
    "content": "This is file3 content"
}
Contents of 'root/': ['folder1', 'folder2']
Contents of 'root/folder1/subfolder2': ['file1.txt', 'file2.txt']
{
    "root": {
        "folder1": {
            "subfolder1": {},
            "subfolder2": {
                "file1.txt": "This is file1 content",
                "file2.txt": "This is file2 content"
            },
            "file3.txt": "This is file3 content"
        },
        "folder2": {
            "subfolder3": {
                "file4.txt": "This is file4 content"
            }
        }
    }
}
"""

## create_dir, create_file, delete_item, move_item, copy_item, update_file_content, search
def create_dir(filesystem, path, dir_name):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                raise ValueError(f"Error: '{path}' not found in filesystem")
        
        if dir_name in current_dir:
            raise ValueError(f"Directory '{dir_name}' already exists at '{path}'")
        
        current_dir[dir_name] = {}
        print(f"Directory '{dir_name}' created at '{path}'")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Example usage
create_dir(filesystem, "root/folder1", "new_folder")

def create_file(filesystem, path, file_name, content):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                raise ValueError(f"Error: '{path}' not found in filesystem")
        
        if file_name in current_dir:
            raise ValueError(f"File '{file_name}' already exists at '{path}'")
        
        current_dir[file_name] = content
        print(f"File '{file_name}' created at '{path}' with content: {content}")
    except Exception as e:
        print(f"Error creating file: {e}")

# Example usage
create_file(filesystem, "root/folder1", "new_file.txt", "This is new file content")

def delete_item(filesystem, path):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts[:-1]:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                raise ValueError(f"Error: '{'/'.join(path_parts[:-1])}' not found in filesystem")
        
        item_name = path_parts[-1]
        if item_name in current_dir:
            del current_dir[item_name]
            print(f"Item '{item_name}' deleted from '{'/'.join(path_parts[:-1])}'")
        else:
            raise ValueError(f"Item '{item_name}' not found at '{'/'.join(path_parts[:-1])}'")
    except Exception as e:
        print(f"Error deleting item: {e}")

# Example usage
delete_item(filesystem, "root/folder1/new_file.txt")

def move_item(filesystem, src_path, dest_path):
    try:
        src_parts = src_path.strip("/").split("/")
        dest_parts = dest_path.strip("/").split("/")
        
        current_src_dir = filesystem
        for part in src_parts[:-1]:
            if part in current_src_dir:
                current_src_dir = current_src_dir[part]
            else:
                raise ValueError(f"Error: '{'/'.join(src_parts[:-1])}' not found in filesystem")
        
        item_name = src_parts[-1]
        if item_name not in current_src_dir:
            raise ValueError(f"Item '{item_name}' not found at '{'/'.join(src_parts[:-1])}'")
        
        current_dest_dir = filesystem
        for part in dest_parts:
            if part in current_dest_dir:
                current_dest_dir = current_dest_dir[part]
            else:
                raise ValueError(f"Error: '{'/'.join(dest_parts)}' not found in filesystem")
        
        current_dest_dir[item_name] = current_src_dir.pop(item_name)
        print(f"Item '{item_name}' moved from '{src_path}' to '{dest_path}'")
    except Exception as e:
        print(f"Error moving item: {e}")

# Example usage
move_item(filesystem, "root/folder1/new_file.txt", "root/folder2/subfolder3")

import copy

def copy_item(filesystem, src_path, dest_path):
    try:
        src_parts = src_path.strip("/").split("/")
        dest_parts = dest_path.strip("/").split("/")
        
        current_src_dir = filesystem
        for part in src_parts[:-1]:
            if part in current_src_dir:
                current_src_dir = current_src_dir[part]
            else:
                raise ValueError(f"Error: '{'/'.join(src_parts[:-1])}' not found in filesystem")
        
        item_name = src_parts[-1]
        if item_name not in current_src_dir:
            raise ValueError(f"Item '{item_name}' not found at '{'/'.join(src_parts[:-1])}'")
        
        current_dest_dir = filesystem
        for part in dest_parts:
            if part in current_dest_dir:
                current_dest_dir = current_dest_dir[part]
            else:
                raise ValueError(f"Error: '{'/'.join(dest_parts)}' not found in filesystem")
        
        current_dest_dir[item_name] = copy.deepcopy(current_src_dir[item_name])
        print(f"Item '{item_name}' copied from '{src_path}' to '{dest_path}'")
    except Exception as e:
        print(f"Error copying item: {e}")

# Example usage
copy_item(filesystem, "root/folder1/file3.txt", "root/folder2/subfolder3")

def update_file_content(filesystem, path, new_content):
    try:
        path_parts = path.strip("/").split("/")
        current_dir = filesystem
        for part in path_parts[:-1]:
            if part in current_dir:
                current_dir = current_dir[part]
            else:
                raise ValueError(f"Error: '{'/'.join(path_parts[:-1])}' not found in filesystem")
        
        file_name = path_parts[-1]
        if file_name in current_dir and not isinstance(current_dir[file_name], dict):
            current_dir[file_name] = new_content
            print(f"File '{file_name}' at '{'/'.join(path_parts[:-1])}' updated with new content: {new_content}")
        else:
            raise ValueError(f"File '{file_name}' not found or is a directory at '{'/'.join(path_parts[:-1])}'")
    except Exception as e:
        print(f"Error updating file content: {e}")

# Example usage
update_file_content(filesystem, "root/folder1/file3.txt", "Updated content for file3")

pretty_print_json(filesystem)

def search(filesystem, name, current_path=""):
    results = []
    for key, value in filesystem.items():
        if key == name:
            results.append(current_path + "/" + key)
        if isinstance(value, dict):
            results.extend(search(value, name, current_path + "/" + key))
    return results

# Example usage
search_results = search(filesystem, "file1.txt")
print(f"Search results for 'file1.txt': {search_results}")

search_results = search(filesystem, "file3.txt")
print(f"Search results for 'file3.txt': {search_results}")

search_results = search(filesystem, "subfolder2")
print(f"Search results for 'subfolder2': {search_results}")

"""
Error creating directory: Directory 'new_folder' already exists at 'root/folder1'
File 'new_file.txt' created at 'root/folder1' with content: This is new file content
Item 'new_file.txt' deleted from 'root/folder1'
Error moving item: Item 'new_file.txt' not found at 'root/folder1'
Item 'file3.txt' copied from 'root/folder1/file3.txt' to 'root/folder2/subfolder3'
File 'file3.txt' at 'root/folder1' updated with new content: Updated content for file3
{
    "root": {
        "folder1": {
            "subfolder1": {},
            "subfolder2": {
                "file1.txt": "This is file1 content",
                "file2.txt": "This is file2 content"
            },
            "file3.txt": "Updated content for file3",
            "new_folder": {}
        },
        "folder2": {
            "subfolder3": {
                "file4.txt": "This is file4 content",
                "file3.txt": "Updated content for file3"
            }
        }
    }
}
Search results for 'file1.txt': ['/root/folder1/subfolder2/file1.txt']
Search results for 'file3.txt': ['/root/folder1/file3.txt', '/root/folder2/subfolder3/file3.txt']
Search results for 'subfolder2': ['/root/folder1/subfolder2']
"""
