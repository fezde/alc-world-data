import json

import yaml
from jsonschema import validate

with open("data-schema.json", "r") as f:
    schema = json.load(f)

with open("data.yaml", "r") as f:
    good_instance = f.read()


validate(yaml.safe_load(good_instance), schema)
