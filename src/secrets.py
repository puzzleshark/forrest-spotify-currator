import os

PLAYLIST_ID = os.popen("bashio::config 'playlist_id'").read().strip()
CLIENT_ID = os.popen("bashio::config 'client_id'").read().strip()
CLIENT_SECRET = os.popen("bashio::config 'client_secret'").read().strip()
USERNAME = os.popen("bashio::config 'username'").read().strip()
PASSWORD = os.popen("bashio::config 'password'").read().strip()
SUPERVISOR_TOKEN = os.getenv("SUPERVISOR_TOKEN")