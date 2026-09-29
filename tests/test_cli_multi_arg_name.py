from samplecli.cli import main
from samplecli.greet import greet


def test_two_args_joined_with_one_space(capsys):
    assert main(["Ada", "Lovelace"]) == 0
    assert capsys.readouterr().out == "Hello, Ada Lovelace!\n"


def test_three_args_joined_in_order(capsys):
    assert main(["Ada", "King", "Lovelace"]) == 0
    assert capsys.readouterr().out == "Hello, Ada King Lovelace!\n"


def test_joined_args_are_stripped_and_collapsed(capsys):
    assert main(["  Ada ", "\tKing  ", " Lovelace\n"]) == 0
    assert capsys.readouterr().out == "Hello, Ada King Lovelace!\n"


def test_blank_args_are_skipped_between_words(capsys):
    assert main(["Ada", "", "   ", "Lovelace"]) == 0
    assert capsys.readouterr().out == "Hello, Ada Lovelace!\n"


def test_all_blank_args_fall_back_to_world(capsys):
    assert main(["", "  ", "\t"]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_single_arg_unchanged(capsys):
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_greet_is_unchanged():
    assert greet("Ada  Lovelace") == "Hello, Ada  Lovelace!"
