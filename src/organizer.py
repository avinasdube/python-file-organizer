from pathlib import Path
import shutil

from scanner import scan_directory
from classifier import get_file_category

def create_category_directory(base_dir: Path, category: str) -> Path:
    """Create and return the directory for a file category."""
    category_directory = base_dir / category
    category_directory.mkdir(exist_ok=True)
    return category_directory

def get_unique_destination(file: Path, destination_directory: Path) -> Path:
    """Return a destination path that doesn't overwrite existing file."""
    destination = destination_directory / file.name
    counter = 1
    while destination.exists():
        destination = destination_directory / f"{file.stem}_{counter}{file.suffix}"
        counter += 1

    return destination

def move_file(file: Path, destination_directory: Path) -> None:
    """Move a file to the specified destination directory."""
    unique_dest = get_unique_destination(file, destination_directory)
    shutil.move(file, unique_dest)

def organize_directory(directory: Path) -> None:
    """Organize files in the given directory."""
    files = scan_directory(directory)
    for file in files:
        category = get_file_category(file)
        category_directory = create_category_directory(directory, category)
        move_file(file, category_directory)

organize_directory(Path("downloads"))
