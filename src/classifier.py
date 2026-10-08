from pathlib import Path

categories = {
    ".jpg": "Images",
    ".pdf": "PDFs",
    ".py": "Code",
    ".mp3": "Audio",
    ".mp4": "Videos"
}

def get_category(extension: str) -> str:
    """Determine the category for a file extension."""
    ext = extension.lower()
    return categories.get(ext, "Others")

def get_file_category(file_path: Path) -> str:
    """Determine the category for a file based on its extension."""
    suff = file_path.suffix
    return get_category(suff)


