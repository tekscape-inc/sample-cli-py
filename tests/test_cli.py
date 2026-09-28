from samplecli.cli import main


def test_main_returns_zero(capsys):
    assert main(["x"]) == 0
    assert capsys.readouterr().out.strip() != ""
