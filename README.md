# Spotify Forrest Music Currator

## Prerequisites

You have a spotify account, and a spotify developer account. In your spotify developer account create a new app, with the redirect uri of http://127.0.0.1:9090.

Copy the <CLIENT_ID> and <CLIENT_SECRET>. You will need those later. Next get the id of the spotify playlist you'd like to currate.

## Running

### Method 1
create a file called **secrets.yaml** in the **src** folder, and put the contents
```
PLAYLIST_ID: <PLAYLIST_ID>
CLIENT_ID: <CLIENT_ID>
CLIENT_SECRET: <CLIENT_SECRET>
USERNAME: <USERNAME>
PASSWORD: <PASSWORD>
```
with the relevant information.

### Method 2
You must build the docker container with `docker build . --tag currator`
run `docker run -e PLAYLIST_ID='<PLAYLIST_ID>'  -e CLIENT_ID='<CLIENT_ID>' -e CLIENT_SECRET='<CLIENT_SECRET'> -e USERNAME='<USERNAME>' -e PASSWORD='<PASSWORD>' currator`
