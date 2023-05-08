import argparse

from models import Query
from stream import find


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="JustWatch CLI")
    parser.add_argument(
        "-c",
        "--country",
        type=str,
        required=True,
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


def main() -> None:
    args = _parse_args()

    country = args.country.upper()
    query = Query(value=args.query, region=country)
    print(find(query=query.value, region=query.region))


if __name__ == "__main__":
    main()
