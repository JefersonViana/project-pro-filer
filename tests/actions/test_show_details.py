from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import datetime


def test_show_details_with_directory(capsys, tmp_path):
    directory = tmp_path / "projetos"
    directory.mkdir()
    date = datetime.fromtimestamp(directory.stat().st_mtime).date()
    size = directory.stat().st_size
    context = {
        "base_path": directory.as_posix()
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == ("File name: projetos\n"
                            f"File size in bytes: {size}\n"
                            "File type: directory\n"
                            "File extension: [no extension]\n"
                            "Last modified date:"
                            f" {date.year}-{date.month}-{date.day}\n")


def test_show_details_with_file(capsys, tmp_path):
    file = tmp_path / "requirements.json"
    file.touch()
    date = datetime.fromtimestamp(file.stat().st_mtime).date()
    size = file.stat().st_size
    context = {
        "base_path": file.as_posix()
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == ("File name: requirements.json\n"
                            f"File size in bytes: {size}\n"
                            "File type: file\n"
                            "File extension: .json\n"
                            "Last modified date: "
                            f"{date.year}-{date.month}-{date.day}\n")


def test_show_details_with_file_not_exist(capsys):
    context = {
        "base_path": "python-029"
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == ("File 'python-029' does not exist\n")
