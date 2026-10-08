from src.organizer import organize_directory, get_unique_destination
from src.exceptions import InvalidDirectoryError

import pytest

def test_organize_image_file(tmp_path):
    test_file = tmp_path / "photo.jpg"
    test_file.touch()

    organize_directory(tmp_path)

    destination = tmp_path / "Images" / "photo.jpg"

    assert destination.exists()
    assert not test_file.exists()

def test_duplicate_filename_gets_unique_name(tmp_path):
    test_file = tmp_path / "photo.jpg"
    test_file.touch()

    images_directory = tmp_path / "Images"
    images_directory.mkdir()

    existing_file = images_directory / "photo.jpg"
    existing_file.touch()

    organize_directory(tmp_path)

    duplicate_destination = images_directory / "photo_1.jpg"

    assert existing_file.exists()
    assert duplicate_destination.exists()
    assert not test_file.exists()


def test_organize_multiple_file_types(tmp_path):
    files = [
        tmp_path / "photo.jpg",
        tmp_path / "report.pdf",
        tmp_path / "song.mp3",
        tmp_path / "script.py",
    ]

    for file in files:
        file.touch()

    organize_directory(tmp_path)

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert (tmp_path / "PDFs" / "report.pdf").exists()
    assert (tmp_path / "Audio" / "song.mp3").exists()
    assert (tmp_path / "Code" / "script.py").exists()

def test_unknown_file_goes_to_others(tmp_path):
    test_file = tmp_path / "mystery.xyz"
    test_file.touch()

    organize_directory(tmp_path)

    destination = tmp_path / "Others" / "mystery.xyz"

    assert destination.exists()
    assert not test_file.exists()


def test_nonexistent_directory_raises_error(tmp_path):
    missing_directory = tmp_path / "does_not_exist"

    with pytest.raises(InvalidDirectoryError):
        organize_directory(missing_directory)

def test_file_path_raises_error(tmp_path):
    test_file = tmp_path / "photo.jpg"
    test_file.touch()

    with pytest.raises(InvalidDirectoryError):
        organize_directory(test_file)

def test_unique_destination_when_no_duplicate(tmp_path):
    test_file = tmp_path / "photo.jpg"

    destination = get_unique_destination(test_file, tmp_path)

    assert destination == tmp_path / "photo.jpg"

def test_unique_destination_adds_counter(tmp_path):
    test_file = tmp_path / "photo.jpg"

    existing_file = tmp_path / "photo.jpg"
    existing_file.touch()

    destination = get_unique_destination(test_file, tmp_path)

    assert destination == tmp_path / "photo_1.jpg"

def test_unique_destination_skips_multiple_duplicates(tmp_path):
    test_file = tmp_path / "photo.jpg"

    (tmp_path / "photo.jpg").touch()
    (tmp_path / "photo_1.jpg").touch()

    destination = get_unique_destination(test_file, tmp_path)

    assert destination == tmp_path / "photo_2.jpg"
