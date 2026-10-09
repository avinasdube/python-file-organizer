import pytest

from file_organizer import organizer
from file_organizer.organizer import organize_directory, get_unique_destination
from file_organizer.exceptions import InvalidDirectoryError, FileOrganizationError


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



from pathlib import Path

from file_organizer.organizer import organize_directory


def test_organize_empty_directory(tmp_path):
    """An empty directory is organized without errors."""
    organize_directory(tmp_path)

    assert list(tmp_path.iterdir()) == []


def test_organize_directory_with_only_subdirectories(tmp_path):
    """Existing subdirectories are not treated as files."""
    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()

    organize_directory(tmp_path)

    assert nested_dir.is_dir()
    assert list(tmp_path.iterdir()) == [nested_dir]


def test_organize_file_without_extension(tmp_path):
    """A file without an extension is placed in Others."""
    file_path = tmp_path / "README"
    file_path.write_text("Sample content", encoding="utf-8")

    organize_directory(tmp_path)

    destination = tmp_path / "Others" / "README"

    assert destination.is_file()
    assert destination.read_text(encoding="utf-8") == "Sample content"


def test_organize_directory_with_existing_category_folder(tmp_path):
    """An existing category directory is reused."""
    images_dir = tmp_path / "Images"
    images_dir.mkdir()

    photo = tmp_path / "photo.jpg"
    photo.write_text("image content", encoding="utf-8")

    organize_directory(tmp_path)

    assert (images_dir / "photo.jpg").is_file()
    assert (images_dir / "photo.jpg").read_text(encoding="utf-8") == (
        "image content"
    )



def test_move_file_raises_error_when_move_fails(tmp_path, monkeypatch):
    """A filesystem movement failure becomes FileOrganizationError."""
    source = tmp_path / "sample.txt"
    source.write_text("sample", encoding="utf-8")

    destination_dir = tmp_path / "Documents"
    destination_dir.mkdir()

    def fake_move(source_path, destination_path):
        raise OSError("Simulated movement failure")

    monkeypatch.setattr(organizer.shutil, "move", fake_move)

    with pytest.raises(FileOrganizationError) as exc_info:
        organizer.move_file(source, destination_dir)

    assert "Could not move" in str(exc_info.value)
    assert isinstance(exc_info.value.__cause__, OSError)
