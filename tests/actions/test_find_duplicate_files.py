from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


@pytest.mark.parametrize(
        "context, result",
        [
            (
                {
                    "all_files": [
                        "pro_filer/cli.py",
                        "pro_filer/cli.py"
                    ]
                },
                [("pro_filer/cli.py", "pro_filer/cli.py")]
            ),
            (
                {
                    "all_files": [
                        "pro_filer/cli.py",
                        "pro_filer/cli_helpers.py"
                    ]
                },
                []
            )
        ]
)
def test_find_duplicate_files(context, result):
    response = find_duplicate_files(context)
    assert response == result


def test_find_duplicate_files_if_launch_error():
    context = {
        "all_files": ["pro_filer/cli.py", "pro_filer/cli_hexlpers.py"]
    }
    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
