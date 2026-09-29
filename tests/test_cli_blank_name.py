from samplecli.cli import main
from samplecli.greet import greet


def test_spaces_only_name_falls_back_to_world(capsys):
    assert main(["   "]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_empty_name_falls_back_to_world(capsys):
    assert main([""]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_tab_newline_name_falls_back_to_world(capsys):
    assert main(["\t\n "]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_name_is_stripped_in_cli(capsys):
    assert main(["  Ada\t"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_greet_does_not_strip_or_default():
    assert greet("  Ada  ") == "Hello,   Ada  !"
    assert greet("") == "Hello, !"
