from samplecli.greet import greet


def test_greet_formats_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_default_world():
    assert greet("world") == "Hello, world!"
