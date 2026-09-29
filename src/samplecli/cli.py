import argparse
import sys

from samplecli.greet import greet


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs="*", default=[])
    parser.add_argument("--repeat", type=int, default=1)
    parsed = parser.parse_args(args)
    if parsed.repeat < 1:
        parser.error("--repeat must be at least 1")
    name = (" ".join(" ".join(parsed.name).split()) if parsed.name else "") or "world"
    for _ in range(parsed.repeat):
        print(greet(name))
    return 0
