import argparse

from stream import SteamerFinder
from models import Query, Result


def _parse_args():
    parser = argparse.ArgumentParser(description="JustWatch CLI")
    parser.add_argument(
        "-c",
        "--country",
        type=str,
        default="ES",
        help="Country code to search in JustWatch",
    )
    parser.add_argument(
        "-q",
        "--query",
        type=str,
        required=True,
        help="Movie or show title to search in JustWatch",
    )

    return parser.parse_args()


def main():
    args = _parse_args()

    query = Query(args.query)
    result = SteamerFinder(args.country, query)
    print(Result(result.title, result.get_platforms()).__dict__)


if __name__ == "__main__":
    main()
