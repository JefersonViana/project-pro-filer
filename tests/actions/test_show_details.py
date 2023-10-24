from pro_filer.actions.main_actions import show_details  # NOQA
import pytest

BASE_URL = ("/home/jeferson-viana/TRYBE/projetos/"
            "python-029-python-projeto-pro-filer")
DIRECTORY = "/.trybe"
FILE = "/requirements.json"


@pytest.mark.parametrize(
        "context, result",
        [
            (
                {
                    "base_path": BASE_URL + DIRECTORY,
                },
                ("File name: .trybe\n"
                 "File size in bytes: 4096\n"
                 "File type: directory\n"
                 "File extension: [no extension]\n"
                 "Last modified date: 2023-10-23\n")
            ),
            (
                {
                    "base_path": BASE_URL + DIRECTORY + FILE,
                },
                ("File name: requirements.json\n"
                 "File size in bytes: 1415\n"
                 "File type: file\n"
                 "File extension: .json\n"
                 "Last modified date: 2023-10-23\n")
            ),
            (
                {
                    "base_path": ("/home/TRYBE/"
                                  "python-029-python-projeto-pro-filer"),
                },
                ("File 'python-029-python-projeto-pro-filer' does not exist\n")
            )
        ]
)
def test_show_details(capsys, context, result):
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == result
