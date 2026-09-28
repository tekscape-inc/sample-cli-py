from samplecli.greet import greet


def test_ci_smoke_greets():
    assert greet("CI") == "Hello, CI!"
