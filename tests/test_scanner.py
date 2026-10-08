from pathlib import Path

from src.scanner import scan_directory

def test_scan_directory_finds_files(tmp_path):
    test_file = tmp_path / "photo.jpg"
    test_file.touch()

    files = scan_directory(tmp_path)

    assert test_file in files

def test_scan_directory_ignores_directories(tmp_path):
    test_file = tmp_path / "photo.jpg"
    test_file.touch()

    test_directory = tmp_path / "subfolder"
    test_directory.mkdir()

    files = scan_directory(tmp_path)

    assert test_file in files
    assert test_directory not in files

def test_scan_empty_directory(tmp_path):
    files = scan_directory(tmp_path)

    assert files == []
