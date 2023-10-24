from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest
import json


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


def test_show_details_with_tmp_path(capsys, tmp_path):
    out_put = tmp_path / "out.json"
    with open(out_put, "w", encoding="utf-8") as file:
        file.write(json.dumps({"chave": "value"}))
    context = {
        "all_files": ["/tmp/pytest-of-jeferson-viana/pytest-5"
                      "/test_show0/out.json"]
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    result = ("'/tmp/pytest-of-jeferson-viana/pytest-5/test_show0/out.json'"
              ":          18 (100%)\n"
              "Total size: 18\n")
    assert captured.out == result
