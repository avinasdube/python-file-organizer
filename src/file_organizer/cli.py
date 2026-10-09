import sys
import argparse
from pathlib import Path

from file_organizer.organizer import organize_directory
from file_organizer.exceptions import (
    InvalidDirectoryError,
    FileOrganizationError
)

def create_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by category."
    )

    parser.add_argument(
        "directory",
        help="Directory to organize."
    )

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()
    directory = Path(args.directory)

    try:
        organize_directory(directory)
    except InvalidDirectoryError as error:
        print(f"Error: {error}")
        return 1
    except FileOrganizationError as error:
        print(f"File organization failed: {error}")
        return 1

    print("Files organized successfully!")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
