from pro_filer.actions.main_actions import show_details  # NOQA
# import pytest

# BASE_URL = ("/home/jeferson-viana/TRYBE/projetos/"
#             "python-029-python-projeto-pro-filer")
# DIRECTORY = "/.trybe"
# FILE = "/requirements.json"


# @pytest.mark.parametrize(
#         "context, result",
#         [
#             (
#                 {
#                     "base_path": BASE_URL + DIRECTORY,
#                 },
#                 ("File name: .trybe\n"
#                  "File size in bytes: 4096\n"
#                  "File type: directory\n"
#                  "File extension: [no extension]\n"
#                  "Last modified date: 2023-10-23\n")
#             ),
#             (
#                 {
#                     "base_path": BASE_URL + DIRECTORY + FILE,
#                 },
#                 ("File name: requirements.json\n"
#                  "File size in bytes: 1415\n"
#                  "File type: file\n"
#                  "File extension: .json\n"
#                  "Last modified date: 2023-10-23\n")
#             ),
#             (
#                 {
#                     "base_path": ("/home/TRYBE/"
#                                   "python-029-python-projeto-pro-filer"),
#                 },
#                 ("File 'python-029-python-projeto-pro-filer'
# does not exist\n")
#             )
#         ]
# )
# def test_show_details(capsys, context, result):
#     show_details(context)
#     captured = capsys.readouterr()
#     assert captured.out == result


def test_show_details_with_directory(capsys, tmp_path):
    directory = tmp_path / "projetos"
    directory.mkdir()
    context = {
        "base_path": directory.as_posix()
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == ("File name: projetos\nFile size in bytes: 4096\n"
                            "File type: directory\n"
                            "File extension: [no extension]\n"
                            "Last modified date: 2023-10-24\n")


def test_show_details_with_file(capsys, tmp_path):
    file = tmp_path / "requirements.json"
    file.touch()
    context = {
        "base_path": file.as_posix()
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == ("File name: requirements.json\n"
                            "File size in bytes: 0\n"
                            "File type: file\n"
                            "File extension: .json\n"
                            "Last modified date: 2023-10-24\n")


def test_show_details_with_file_not_exist(capsys):
    context = {
        "base_path": "python-029"
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == ("File 'python-029' does not exist\n")
