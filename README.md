# DirectoryContentCollector

**DirectoryContentCollector** is a Python tool designed to recursively traverse directories, collect file contents, and generate a well-structured Markdown report. It supports customizable filtering for excluding specific files and directories.

---

## Features

- Recursively collects contents from all files in a target directory.
- Filters files and directories based on user-defined rules.
- Skips empty files automatically.
- Outputs the results as a neatly formatted Markdown file.
- Identifies programming languages based on file extensions for syntax highlighting in the Markdown.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mrloic/DirectoryContentCollector.git
   cd DirectoryContentCollector
   ```

2. Ensure Python 3.6 or later is installed.

---

## Usage

1. **Prepare a Filter File**

   Create a filter file (e.g., `filter.txt`) with the following format:

   ```plaintext
   # Exclude directories
   dir: .git
   dir: cache
   dir: vendor

   # Exclude files
   file: .gitignore
   file: composer.lock
   ```

2. **Run the Script**

   Execute the script and provide the required inputs:

   ```bash
   python collect_files.py
   ```

   The program will prompt you for:
   - The path to the target directory to analyze.
   - The path to the filter file.

3. **Output**

   The script generates a Markdown file named `output_<directory_name>.md`, where `<directory_name>` is the name of the analyzed directory. For example:
   ```plaintext
   output_projects.md
   ```

---

## Example

### Target Directory Structure
```plaintext
projects/
├── .git/
├── cache/
├── vendor/
│   └── library.txt
├── script.py
└── README.md
```

### Filter File
```plaintext
# Exclude directories
dir: .git

# Exclude files
file: README.md
```

### Output File (`output_projects.md`)
```markdown
`script.py`
```python
# Example Python script
print("Hello, world!")```
```


---

## Contributing

Contributions are welcome! Please:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

[Mr_LOIC](https://github.com/mrloic)
