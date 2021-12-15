import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import librosa
import numpy as np

import secrets

MP3_FOLDER = 'music'


def download_playlist(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    os.system(f'spotdl https://open.spotify.com/playlist/{secrets.PLAYLIST_ID} -o {folder_name}')
    return os.listdir(folder_name)


def get_filename(track, filenames):
    for filename in filenames:
        if track['name'].strip('?') in filename:
            return os.path.join("music", filename)


def song_in_tune(filename):
    y, sr = librosa.load(filename, duration=40)
    value = librosa.estimate_tuning(y=y, sr=sr)
    cents = round(value * 100)
    if cents < 0:
        print(f'{np.abs(cents)} cents flat')
    else:
        print(f'{np.abs(cents)} cents sharp')
    if np.abs(cents) > 9:  # needs to be better than 9 cents
        print("not good enough")
        return False
    else:
        return True


if __name__ == '__main__':

    filenames = download_playlist(MP3_FOLDER)

    auth = SpotifyOAuth(
        scope=["playlist-modify-public", "playlist-modify-private"],
        username=secrets.USERNAME,
        client_id=secrets.CLIENT_ID,
        client_secret=secrets.CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:9090",
        open_browser=False,
    )

    spotify = spotipy.Spotify(oauth_manager=auth)

    results = spotify.playlist_items(f"spotify:playlist:{secrets.PLAYLIST_ID}")

    for item in results['items']:
        track = item['track']
        print("====================================================================")
        print('track    : ' + track['name'])
        print('audio    : ' + track['uri'])
        filename = get_filename(track, filenames)

        try:
            if not song_in_tune(filename):
                spotify.playlist_remove_all_occurrences_of_items(secrets.PLAYLIST_ID, [track['uri']])
                print("removed it")
        except:
            print("could not parse, need to figure this out")

