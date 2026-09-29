from samplecli.cli import main
from samplecli.greet import greet


def test_greet_shout_uppercases():
    assert greet("Ada", shout=True) == "HELLO, ADA!"


def test_greet_shout_default_off():
    assert greet("Ada") == "Hello, Ada!"


def test_cli_shout_before_name(capsys):
    assert main(["--shout", "Ada"]) == 0
    assert capsys.readouterr().out == "HELLO, ADA!\n"


def test_cli_shout_after_name(capsys):
    assert main(["Ada", "--shout"]) == 0
    assert capsys.readouterr().out == "HELLO, ADA!\n"


def test_cli_shout_default_name(capsys):
    assert main(["--shout"]) == 0
    assert capsys.readouterr().out == "HELLO, WORLD!\n"
