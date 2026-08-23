# 01. json — the `s` suffix means string: dumps/loads vs dump/load
# Run: python 01_json_basics.py



# dumps: object -> JSON string        loads: JSON string -> object
# dump:  object -> file               load:  file -> object
import json

payload = {"person_id": 124, "tags": ["a", "b"], "active": True, "score": None}
text = json.dumps(payload)
print(text)
print(json.loads(text) == payload)



# file round-trip
from pathlib import Path

path = Path(__file__).with_name("scratch.json")
with path.open("w") as f:
    json.dump(payload, f, indent=4)

with path.open() as f:
    data = json.load(f)
print(data["person_id"])
print(path.read_text()[:20].replace("\n", "\\n"))



# type mapping: dict->object, list/tuple->array, None->null, True->true
print(json.dumps({"t": (1, 2), "n": None, "b": False}))
print(type(json.loads("[1, 2]")), json.loads("null"))



# non-serializable types raise TypeError — pass a default= fallback
import datetime

record = {"when": datetime.datetime(2026, 8, 23, 10, 30)}
try:
    json.dumps(record)
except TypeError as e:
    print("TypeError:", e)

print(json.dumps(record, indent=4, sort_keys=True, default=str))



# or supply a function for custom encoding
def encode(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"not serializable: {type(obj).__name__}")


print(json.dumps(record, default=encode))



# gotchas: dict keys are coerced to strings, and non-string keys round-trip differently
print(json.dumps({1: "a"}), json.loads(json.dumps({1: "a"})))



# embedding JSON in Python source: triple quotes (JSON often holds single quotes)
raw = """{"name": "it's fine", "path": "C:\\\\tmp"}"""
print(json.loads(raw))



# a JSON backslash is also an escape — use a raw string for literals containing them
print(json.loads(r'{"re": "\\d+"}'))
try:
    json.loads('{"bad": "\\d+"}')
except json.JSONDecodeError as e:
    print("JSONDecodeError:", e.msg)



# handy helper
def write_json(data, file_path):
    Path(file_path).write_text(json.dumps(data, indent=4))


write_json(payload, path)
print(json.loads(path.read_text())["tags"])
path.unlink()



# Practice
# Q1. Write a decoder hook (object_hook=) that turns ISO strings back into datetimes.
# Q2. Why does json.dumps(set()) fail, and what is the simplest fix?
# Q3. Compare json.dumps(d, indent=2) with pprint for inspecting nested data.
