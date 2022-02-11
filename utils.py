import yaml, os, re
from typing import List

def get_config():
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(script_path + "/config.yaml") as stream:
        config = yaml.safe_load(stream)
    return config

def extract(pattern: str, txt: str) -> List[str]:
    return re.findall(pattern, txt, re.IGNORECASE)

