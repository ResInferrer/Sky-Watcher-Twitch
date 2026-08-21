import json
import os

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
    'private_config.json'
)

def load_config():
    if not os.path.exists(CONFIG_PATH):
        print(f"Error: {CONFIG_PATH} file not found.") # TODO: norm error log!
        exit(1)
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

config = load_config()
SERVER = config["server"]
PORT = config["port"]
NICKNAME = config["nickname"]
TOKEN = config["token"]
CHANNEL = config["channel"]