from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
        ["context", "result"],
        [
            (
                {
                    "all_files": ["src/__init__.py",
                                  "src/app.py", "src/utils/__init__.py"],
                    "all_dirs": ["src", "src/utils"]
                },
                (
                    "Found 3 files and 2 directories\n"
                    "First 5 files: ['src/__init__.py', 'src/app.py', "
                    "'src/utils/__init__.py']\n"
                    "First 5 directories: ['src', 'src/utils']\n"
                )
            ),
            (
                {
                    "all_files": [],
                    "all_dirs": []
                },
                ("Found 0 files and 0 directories\n")
            ),
            (
                {"all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                    "src/todo_list.py",
                    "src/users.py",
                    "src/login.py"
                ],
                    "all_dirs": ["src", "src/utils"]},
                (
                    "Found 6 files and 2 directories\n"
                    "First 5 files: ['src/__init__.py', 'src/app.py', "
                    "'src/utils/__init__.py', "
                    "'src/todo_list.py', "
                    "'src/users.py']\n"
                    "First 5 directories: ['src', 'src/utils']\n"
                )
            )
        ]
)
def test_show_preview(capsys, context, result):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == result
