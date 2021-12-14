import os

if os.path.isfile("secrets.yaml"):
    from ruamel.yaml import YAML
    yaml = YAML(typ="safe")
    secrets = yaml.load("secrets.yaml")
else:
    secrets = {}

PLAYLIST_ID = secrets["PLAYLIST_ID"] if "PLAYLIST_ID" in secrets.keys() else os.getenv("PLAYLIST_ID")
CLIENT_ID = secrets["CLIENT_ID"] if "CLIENT_ID" in secrets.keys() else os.getenv("CLIENT_ID")
CLIENT_SECRET = secrets["CLIENT_SECRET"] if "CLIENT_SECRET" in secrets.keys() else os.getenv("CLIENT_SECRET")
USERNAME = secrets["USERNAME"] if "USERNAME" in secrets.keys() else os.getenv("USERNAME")
PASSWORD = secrets["PASSWORD"] if "PASSWORD" in secrets.keys() else os.getenv("PASSWORD")