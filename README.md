# Spotify Forrest Music Curator

## Prerequisites

You have a spotify account, and a spotify developer account. In your spotify developer account create a new app, with the redirect uri of "fdsifds".

Get the client_id and client_secret. You will need those later. Next get the id of the spotify playlist you'd like to currate.

## Running

### Method 1
what

### Method 2
You must build the docker container with `docker build . --tag currator`
run `docker run -e CLIENT_ID='<CLIENT_ID>' -e currator`
