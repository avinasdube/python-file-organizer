import pytest

from file_organizer import cli
from file_organizer.exceptions import (
    InvalidDirectoryError,
    FileOrganizationError,
)


def test_main_success(monkeypatch, capsys):
    """The CLI prints a success message when organization succeeds."""
    monkeypatch.setattr(
        cli,
        "organize_directory",
        lambda directory: None,
    )
    monkeypatch.setattr(
        cli.sys,
        "argv",
        ["file-organizer", "test_folder"],
    )

    cli.main()

    captured = capsys.readouterr()
    assert "Files organized successfully!" in captured.out
    assert captured.err == ""



def test_main_invalid_directory(monkeypatch, capsys):
    """The CLI returns code 1 when the directory is invalid."""
    def raise_invalid_directory(directory):
        raise InvalidDirectoryError("Directory does not exist.")

    monkeypatch.setattr(
        cli,
        "organize_directory",
        raise_invalid_directory,
    )
    monkeypatch.setattr(
        cli.sys,
        "argv",
        ["file-organizer", "missing_folder"],
    )

    exit_code = cli.main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Error: Directory does not exist." in captured.out
    assert "successfully" not in captured.out.lower()



def test_main_organization_error(monkeypatch, capsys):
    """The CLI returns code 1 when file organization fails."""
    def raise_organization_error(directory):
        raise FileOrganizationError("Could not move file.")

    monkeypatch.setattr(
        cli,
        "organize_directory",
        raise_organization_error,
    )
    monkeypatch.setattr(
        cli.sys,
        "argv",
        ["file-organizer", "test_folder"],
    )

    exit_code = cli.main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "File organization failed: Could not move file." in captured.out


def test_main_passes_directory_to_organizer(monkeypatch, capsys):
    """The CLI converts the supplied path into a Path object."""
    received = {}

    def fake_organize_directory(directory):
        received["directory"] = directory

    monkeypatch.setattr(
        cli,
        "organize_directory",
        fake_organize_directory,
    )
    monkeypatch.setattr(
        cli.sys,
        "argv",
        ["file-organizer", "my_folder"],
    )

    cli.main()

    assert str(received["directory"]) == "my_folder"
    assert received["directory"].is_absolute() is False


def test_main_missing_argument(monkeypatch, capsys):
    """Argparse exits with an error when no directory is supplied."""
    monkeypatch.setattr(
        cli.sys,
        "argv",
        ["file-organizer"],
    )

    with pytest.raises(SystemExit) as exc_info:
        cli.main()

    captured = capsys.readouterr()

    assert exc_info.value.code == 2
    assert "usage:" in captured.err.lower()
    assert "directory" in captured.err.lower()


def test_main_help(monkeypatch, capsys):
    """The CLI displays help and exits successfully."""
    monkeypatch.setattr(
        cli.sys,
        "argv",
        ["file-organizer", "--help"],
    )

    with pytest.raises(SystemExit) as exc_info:
        cli.main()

    captured = capsys.readouterr()

    assert exc_info.value.code == 0
    assert "usage:" in captured.out.lower()
    assert "directory" in captured.out.lower()
    assert "Organize files in a directory" in captured.out
