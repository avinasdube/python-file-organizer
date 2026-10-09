from pathlib import Path

def scan_directory(directory: Path) -> list[Path] :
    """Scan the given directory and list files."""
    files = []
    for item in directory.iterdir():
        if item.is_file():
            files.append(item)
    return files

