import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent.parent.parent / 'private_config.json'

def load_config():
    if not CONFIG_PATH.exists():
        print(f"Error: {CONFIG_PATH} file not found.") # TODO: norm error log!
        exit(1)
    
    with CONFIG_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

config = load_config()
SERVER = config["server"]
PORT = config["port"]
NICKNAME = config["nickname"]
TOKEN = config["token"]
CHANNEL = config["channel"]