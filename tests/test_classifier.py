from pathlib import Path
from src.classifier import get_category, get_file_category

def test_jpg_is_image():
    assert get_category(".jpg") == "Images"

def test_pdf_is_pdf():
    assert get_category(".pdf") == "PDFs"

def test_uppercase_extension_is_supported():
    assert get_category(".PDF") == "PDFs"

def test_unknown_extension_is_other():
    assert get_category(".xyz") == "Others"

def test_empty_extension_is_other():
    assert get_category("") == "Others"

def test_file_path_is_classified():
    file_path = Path("photo.jpg")

    assert get_file_category(file_path) == "Images"
