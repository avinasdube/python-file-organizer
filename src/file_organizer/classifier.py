from pathlib import Path

categories = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    # Documents
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",

    # PDFs
    ".pdf": "PDFs",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".webm": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # Code
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".jsx": "Code",
    ".tsx": "Code",
    ".html": "Code",
    ".css": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".php": "Code",
    ".sql": "Code",
}

def get_category(extension: str) -> str:
    """Determine the category for a file extension."""
    ext = extension.lower()
    return categories.get(ext, "Others")

def get_file_category(file_path: Path) -> str:
    """Determine the category for a file based on its extension."""
    extension = file_path.suffix
    return get_category(extension)


