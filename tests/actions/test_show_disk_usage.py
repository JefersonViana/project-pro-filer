from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest
from unittest.mock import Mock, patch


@pytest.mark.parametrize(
        "context, result",
        [
            (
                {
                    "all_files": [
                        "pro_filer/cli.py",
                        "pro_filer/entities.py",
                    ]
                },
                ("'pro_filer/cli.py':"
                 "                                                    3811"
                 " (95%)\n"
                 "'pro_filer/entities.py':"
                 "                                               179"
                 " (4%)\n"
                 "Total size: 3990\n")
            ),
            (
                {
                   "all_files": []
                },
                ("Total size: 0\n")
            )
        ]
)
def test_show_details(capsys, context, result):
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == result


def test_show_disk_with_tmp_path(capsys, tmp_path):
    file_emails = tmp_path / "emails.json"
    file_users = tmp_path / "users.json"
    CONTENT_EMAILS = '{"emails": ["email_fake", "email_fake", "email_fake"]}'
    CONTENT_USERS = '{"users": ["name_fake", "name_fake"]}'
    file_emails.write_text(CONTENT_EMAILS)
    file_users.write_text(CONTENT_USERS)
    # with open(file_emails.as_posix().split("/")[-1], "w") as file:
    #     json.dump({"emails": ["email_fake", "email_fake",
    # "email_fake"]}, file)

    #  CÓDIGO PRECISANDO SER REVISTO.
    # with open(file_users, "w") as file:
    #     json.dump({"users": ["name_fake", "name_fake"]}, file)

    context = {
        "all_files": [
            file_emails.as_posix(),
            file_users.as_posix()
        ]
    }
    mock_return_from_get_printable = Mock(
        return_value=("/tmp/pytest-of-jeferson-via.../"
                      "test_show_disk_with_tmp_path0")
    )
    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path",
        mock_return_from_get_printable
    ):
        show_disk_usage(context)
        captured = capsys.readouterr()
        assert captured.out == (
            "'/tmp/pytest-of-jeferson-via.../test_show_disk_with_tmp_path0':"
            "        54 (59%)\n"
            "'/tmp/pytest-of-jeferson-via.../test_show_disk_with_tmp_path0':"
            "        37 (40%)\n"
            "Total size: 91\n"
        )

        captured = capsys.readouterr()
        assert captured.out != (
            "'/tmp/pytest-of-jeferson-via.../test_show_disk_with_tmp_path0':"
            "        37 (40%)\n"
            "'/tmp/pytest-of-jeferson-via.../test_show_disk_with_tmp_path0':"
            "        54 (59%)\n"
            "Total size: 91\n"
        )
