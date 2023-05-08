import json

from models import Result


def serialize(obj: Result) -> json:
    return json.dumps(obj.__dict__, indent=4, ensure_ascii=False)
