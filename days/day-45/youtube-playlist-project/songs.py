#It fetches the songs from billboard website
import requests
from bs4 import BeautifulSoup
#Constants
WEBSITE_URL="https://www.billboard.com/charts/hot-100/"
HEADER={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

def fetch_website():
    try:
        response=requests.get(url=WEBSITE_URL,headers=HEADER).text
    except Exception as e:
        print(f"Exception {e}")
    return response

def scrape_songs():
    html=fetch_website()
    soup=BeautifulSoup(html,features='html.parser')
    songs=[song.getText().strip() for song in soup.select('li ul li h3')]
    return songs


