#learn about beautiful soup library in python
from bs4 import BeautifulSoup
import requests

with open('C:\\Users\\samar\\Desktop\\software-development\\Python-100-days-journey\\revision\\index.html','r') as f:
    scraper=BeautifulSoup(f,features='html.parser')
#In the above example, i am opening a html file, provinding the contents to a BS funcion, using std HTML parser, to extract contents and turn into objs

print(scraper.prettify()) #prints html code with proper structure
print(scraper.find_all('a')) #Finds all anchor tags 

#Finding links in anchor tags
for i in scraper.find_all(name='a'):
    print(i.get('href'))

print(scraper.find(name='p',attrs='title').string)
#Css selection
print(scraper.select(selector="head title"))

#Scraping a live website
response=requests.get(url="https://news.ycombinator.com/")
html=response.text
soup=BeautifulSoup(html,'html.parser')
title=soup.find('span',attrs='titleline').getText()
print(title)
points=[i.getText().split()[0] for i in soup.find_all(name='span',attrs='score')]
print(list(map(int,points)))



