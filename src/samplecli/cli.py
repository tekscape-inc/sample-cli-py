import sys

from samplecli.greet import greet


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    name = (args[0].strip() if args else "") or "world"
    print(greet(name))
    return 0
