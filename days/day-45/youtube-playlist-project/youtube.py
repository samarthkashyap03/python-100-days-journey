import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from songs import scrape_songs

SCOPES = ["https://www.googleapis.com/auth/youtube"]

def get_youtube_client():
    creds = None
    # token.json stores the user's access and refresh tokens
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials, run the login flow.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # client_secret.json is the OAuth client you downloaded from Google Cloud
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)
#Initialise Youtube client
youtube = get_youtube_client()

def get_playlist_info():
     #Fetch the playlist information
    request = youtube.playlists().list(part="snippet,contentDetails", mine=True)
    response = request.execute()

    items = response.get("items", [])
    for item in items:
        if item['snippet'].get('title')=='Music_playlist':
            return item.get('id')
    return None

def create_playlist():
    #Fetch the playlist information
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Music_playlist",
                "description": "Created via YouTube Data API",
                "tags": ["api", "python"]
            },
            "status": {
                "privacyStatus": "public"   # "public" or "unlisted" also valid
            }
        }
    )
    response=request.execute()
    return response['id']

def search_songs(songs)->list:
    video_ids=[]
    for song in songs:
        request = youtube.search().list(
        part="snippet",
        q=song,
        type="video",
        maxResults=1,
        )
        try:
            response = request.execute()
        except Exception:
            print('Exception Occured')
            continue
        items = response.get("items", [])
        if not items:
            continue
        video_ids.append(items[0]['id']['videoId'])
    return video_ids

def add_video(playlist_id:str,video_id:list):
    for video in video_id:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video
                    }
                }
            }
        )
        try:
            request.execute()
        except Exception:
            print("Cannot insert video!")
            continue
    print('Successfull')

   
