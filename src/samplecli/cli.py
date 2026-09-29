import sys

from samplecli.greet import greet


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    shout = "--shout" in args
    args = [arg for arg in args if arg != "--shout"]
    name = args[0] if args else "world"
    print(greet(name, shout=shout))
    return 0
