# JSON Filesystem Emulator

This project provides a simple emulator for a filesystem represented as a JSON object. It includes functions for various filesystem operations such as listing directories, walking directories, changing directories, and more. Additionally, it includes search functionality to find files or directories by name within the JSON filesystem.

## Features

- List the contents of a directory
- Walk through directories recursively
- Change the current directory
- Retrieve terminal size
- List environment variables
- Show command line arguments and Python search paths
- Display Python system information
- Get the size of files or directories
- Get detailed information about files or directories
- Pretty print JSON data
- Search for files or directories by name

## Installation

No installation required. Simply clone the repository and run the `filesystem.py` script.

## Usage

### Example Filesystem Structure

```python
filesystem = {
    "root": {
        "folder1": {
            "subfolder1": {
                "file1.txt": "Content of file1",
                "file2.txt": "Content of file2"
            },
            "subfolder2": {}
        },
        "folder2": {
            "subfolder3": {
                "file3.txt": "Content of file3"
            }
        },
        "file4.txt": "Content of file4"
    }
}
```

### Features
- load_filesystem, list_dir, walk_dir, get_file_info, pretty_print_json
    - List Directory Contents: List json file structure
    - Walk Directory
    - Retrieve Size and Info of Files or Directories
    - Pretty Print JSON Data
- create_dir, create_file, delete_item, move_item, copy_item, update_file_content, search    
    - Search Paths
    - Item Management: CRUDE

