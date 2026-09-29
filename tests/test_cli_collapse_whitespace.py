from samplecli.cli import main
from samplecli.greet import greet


def test_internal_spaces_collapsed_in_cli(capsys):
    assert main(["Ada   Lovelace"]) == 0
    assert capsys.readouterr().out == "Hello, Ada Lovelace!\n"


def test_mixed_whitespace_run_collapsed_in_cli(capsys):
    assert main(["Ada \t\n Lovelace"]) == 0
    assert capsys.readouterr().out == "Hello, Ada Lovelace!\n"


def test_every_internal_run_collapsed_and_ends_stripped(capsys):
    assert main(["  Ada  King   Lovelace\t"]) == 0
    assert capsys.readouterr().out == "Hello, Ada King Lovelace!\n"


def test_single_spaces_preserved_in_cli(capsys):
    assert main(["Ada Lovelace"]) == 0
    assert capsys.readouterr().out == "Hello, Ada Lovelace!\n"


def test_greet_does_not_collapse_whitespace():
    assert greet("Ada   Lovelace") == "Hello, Ada   Lovelace!"
