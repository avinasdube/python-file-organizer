# 📂 Python File Organizer

A command-line application built with Python that automatically organizes files into category-based folders according to their file extensions.

## ✨ Features

- 🗂️ **Automatic File Classification:** Organizes files into categories based on their extensions.
- 📁 **Multiple Categories:** Supports Images, Documents, PDFs, Videos, Audio, Archives, Code, and Others.
- 🔒 **Duplicate Filename Protection:** Prevents overwriting existing files by generating unique destination filenames.
- ✅ **Path Validation:** Checks whether the supplied path exists and points to a directory.
- ⚠️ **Error Handling:** Provides readable error messages for expected filesystem failures.
- 💻 **Command-Line Interface:** Supports command-line arguments, help output, and meaningful exit codes.
- 🧪 **Automated Testing:** Uses `pytest` to test classification, scanning, file movement, error handling, and CLI behavior.

## 🛠️ Technology Stack

- **Language:** Python 3.13+
- **Filesystem Operations:** `pathlib`, `shutil`
- **Command-Line Interface:** `argparse`
- **Testing:** `pytest`
- **Packaging:** `setuptools`

## 📁 Project Structure

```text
python-file-organizer/
├── src/
│   └── file_organizer/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── classifier.py
│       ├── scanner.py
│       ├── organizer.py
│       └── exceptions.py
├── tests/
│   ├── test_classifier.py
│   ├── test_cli.py
│   ├── test_organizer.py
│   └── test_scanner.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd python-file-organizer
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment using the appropriate command.

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source .venv/Scripts/activate
```

### 3. Install the Project

```bash
python -m pip install -e .
```

### 4. Install Testing Dependencies

```bash
python -m pip install pytest
```

## 💻 Usage

Organize files by providing the path of the target directory.

### Run as a Python Module

```bash
python -m file_organizer "D:\Downloads"
```

### Run Using the Installed Command

```bash
file-organizer "D:\Downloads"
```

### Display Help

```bash
file-organizer --help
```

The application scans files directly inside the specified directory and moves them into category folders. It does not recursively organize files inside nested directories.

> **Note:** The organizer moves files rather than copying them. Test it on a disposable directory before using it on important files.

## 📊 Example

### Before Organization

```text
Downloads/
├── photo.jpg
├── report.pdf
├── notes.txt
└── script.py
```

### After Organization

```text
Downloads/
├── Images/
│   └── photo.jpg
├── PDFs/
│   └── report.pdf
├── Documents/
│   └── notes.txt
└── Code/
    └── script.py
```

Files with unrecognized or missing extensions are placed in the `Others` directory.

## 🧪 Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run tests for a specific module:

```bash
python -m pytest tests/test_organizer.py -v
```

The test suite covers:

- File classification by extension
- Directory scanning
- File movement and duplicate filename handling
- Invalid directory paths
- Empty directories and directories containing subdirectories
- Files without extensions
- Filesystem operation failures
- Command-line arguments, help output, and exit codes

## 🧠 Application Design

The application follows a modular structure, with each module responsible for a specific task.

- **`classifier.py`:** Maps file extensions to categories.
- **`scanner.py`:** Finds files inside the target directory.
- **`organizer.py`:** Validates directories, creates category folders, and moves files.
- **`exceptions.py`:** Defines custom exceptions for application errors.
- **`cli.py`:** Parses command-line arguments, displays messages, and returns exit codes.
- **`__main__.py`:** Enables execution using `python -m file_organizer`.

This separation of responsibilities improves readability, maintainability, and testability.

## 🔮 Future Improvements

- [ ] Add a dry-run mode to preview changes before moving files.
- [ ] Add optional recursive organization.
- [ ] Implement structured logging.
- [ ] Allow users to configure file categories.
- [ ] Display a summary of files moved and skipped.
- [ ] Expand filesystem edge-case test coverage.

## 📄 License

No license has been selected yet. Add an appropriate license before distributing the project publicly.
