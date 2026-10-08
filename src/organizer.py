from pathlib import Path
import shutil

from scanner import scan_directory
from classifier import get_file_category

from exceptions import InvalidDirectoryError, FileOrganizationError


def create_category_directory(base_dir: Path, category: str) -> Path:
    """Create and return the directory for a file category."""
    category_directory = base_dir / category
    try:
        category_directory.mkdir(exist_ok=True)
    except OSError as error:
        raise FileOrganizationError(f"Could not create directory '{category_directory}'.") from error
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
    try:
        shutil.move(file, unique_dest)
    except OSError as error:
        raise FileOrganizationError(f"Could not move '{file}' to '{unique_dest}'.") from error

def organize_directory(directory: Path) -> None:
    """Organize files in the given directory."""
    if not directory.exists():
        raise InvalidDirectoryError("Directory does not exist.")

    if not directory.is_dir():
        raise InvalidDirectoryError("Path is not a directory.")

    files = scan_directory(directory)
    for file in files:
        category = get_file_category(file)
        category_directory = create_category_directory(directory, category)
        move_file(file, category_directory)

try:
    organize_directory(Path("downloads"))
except InvalidDirectoryError as error:
    print(f"Error: {error}")
except FileOrganizationError as error:
    print (f"Error: {error}")
