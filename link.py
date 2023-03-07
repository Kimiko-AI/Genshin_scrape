import requests
from bs4 import BeautifulSoup

url = 'https://genshin-impact.fandom.com/wiki/Category:Inazuma_Quests'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and '/wiki/' in href:
        links.append("https://genshin-impact.fandom.com" + href)

with open(r'E:\Python\Scrape\link.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')