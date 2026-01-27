import requests
from bs4 import BeautifulSoup
HEADERS={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.6",
    }

def get_html_content(URL):
    try:
        response=requests.get(URL,headers=HEADERS)
    except Exception as e:
        print("Check URL")
        return 
    else:
        return response.text
    
def scrape_data(url):
    html_content=get_html_content(url)
    soup=BeautifulSoup(html_content,features='html.parser')
    price_whole=soup.select('span.a-price.aok-align-center span.a-price-whole')[0]
    price_fraction=soup.select('span.a-price.aok-align-center span.a-price-fraction')[0]
    total_price=float(f"{price_whole.text}{price_fraction.text}")
    return int(total_price)
