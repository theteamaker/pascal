import os, json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def metaformat(specifications):

    scopes = ["https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.force-ssl"]
    identifier = str(specifications["batch_identifier"])
    length = int(specifications["length"])

    # Delete this later
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    clients_secrets_file="client_secrets.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        clients_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    game_name = input("Game Name: ")
    composer = input("Composer: ")
    platform = input("Platform: ")

    search_request = youtube.search().list(
        part="snippet",
        forMine=True,
        maxResults=length,
        q=identifier,
        type="video"
    )
    search_response = search_request.execute()

    playlist_request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": game_name,
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "public"
            }
        } 
    )

    playlist_response = playlist_request.execute()
    playlist_id = playlist_response['id']

    with open('../dictionary.json') as openfile:

        loaded_dict = json.load(openfile)

        for song in loaded_dict:
            if song == "thumbnail":
                continue
        
            for num, video in enumerate(search_response["items"]):
                if str(song) in video["snippet"]["title"]:
                    id = video["id"]["videoId"]
                    
                    unformatted_description = (
                        f"Music: {loaded_dict[song]['title']}\n",
                        f"Composer: {composer}\n",
                        f"Playlist: https://www.youtube.com/playlist?list={playlist_id}\n",
                        f"Platform: {platform}\n\n",
                        f"Please read the channel description."
                    )

                    description = ""
                    for item in unformatted_description:
                        description += item
                    
                    update_request = youtube.videos().update(
                        part="snippet",
                        body={
                            "id": id,
                            "snippet": {
                                "categoryId": 10,
                                "defaultLanguage": "en",
                                "description": str(description),
                                "title": f"{loaded_dict[song]['title']} - {game_name}"
                            }
                        }
                    )

                    update_response = update_request.execute()

                    playlist_request = youtube.playlistItems().insert(
                        part="snippet",
                        body={
                            "snippet": {
                                "playlistId": playlist_id,
                                "resourceId": {
                                    "kind": "youtube#video",
                                    "videoId": id
                                }
                            }
                        }
                    )

                    playlist_response = playlist_request.execute()