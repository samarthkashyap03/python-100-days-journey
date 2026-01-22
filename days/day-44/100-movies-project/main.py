#This is a practice project that scrapes the names of 100 movies from a website - 
#https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/ and outputs a txt file
from bs4 import BeautifulSoup
import requests
import html

#Read data from a website
try:
    response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
    html_code=response.text
except requests.exceptions:
    print("Please check the website")


#Initialise BS4
soup=BeautifulSoup(html_code,features='lxml')

movies=[]
#Identify all the movie names and store it as a list
try:
    for movie in soup.find_all(name='h3'):
        movies.append(html.unescape(movie.getText()))
    movies.reverse()
except Exception as e:
    print(f'Exception {e} occured')
else:
    #Write output to a file
    with open('movies.txt','w',encoding='utf-8') as f:
        for i in movies:
            f.write(str(i)+"\n")




