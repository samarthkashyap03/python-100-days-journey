#The aim of this project is to scrape the billboard website for top 100 trending songs.
#Create a playlist with Youtube using its API and search and save those songs in the playlist.
from songs import scrape_songs
import youtube
from songs import scrape_songs

def main():
    #Get playlist info
    playlist_id=youtube.get_playlist_info()
    #If none, create a playlist
    if playlist_id==None:
        playlist_id=youtube.create_playlist()
    #Scrape the songs from the website
    songs=scrape_songs()
    #Search the songs on youtube and collect their video IDs
    video_list=youtube.search_songs(songs)
    #Add the videos to the playlist created
    youtube.add_video(playlist_id,video_list)

#Main Function
main()

    


