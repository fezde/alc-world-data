import json

import yaml
from jsonschema import validate

with open("data/data-schema.json", "r") as f:
    schema = json.load(f)

with open("data/data.yaml", "r") as f:
    good_instance = f.read()

try:
    validate(yaml.safe_load(good_instance), schema)
    exit(0)
except Exception as e:
    print(e)
    exit(1)
