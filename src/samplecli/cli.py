import sys

from samplecli.greet import greet


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    name = (" ".join(args[0].split()) if args else "") or "world"
    print(greet(name))
    return 0
