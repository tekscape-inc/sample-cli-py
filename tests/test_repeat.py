import pytest

from samplecli.cli import main


def _exit_code(argv):
    try:
        return main(argv)
    except SystemExit as exc:
        return exc.code


def test_repeat_prints_greeting_n_times(capsys):
    assert _exit_code(["--repeat", "3", "Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n" * 3


def test_repeat_after_name(capsys):
    assert _exit_code(["Ada", "--repeat", "2"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n" * 2


def test_repeat_one_prints_once(capsys):
    assert _exit_code(["--repeat", "1", "Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_repeat_keeps_name_normalisation(capsys):
    assert _exit_code(["--repeat", "2", "  Ada   Lovelace\t"]) == 0
    assert capsys.readouterr().out == "Hello, Ada Lovelace!\n" * 2


def test_repeat_without_name_greets_world(capsys):
    assert _exit_code(["--repeat", "2"]) == 0
    assert capsys.readouterr().out == "Hello, world!\n" * 2


def test_no_repeat_prints_once(capsys):
    assert _exit_code(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


@pytest.mark.parametrize("n", ["0", "-1", "-5"])
def test_repeat_below_one_is_usage_error(capsys, n):
    assert _exit_code(["--repeat", n, "Ada"]) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.strip() != ""
