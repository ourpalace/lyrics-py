import requests
from bs4 import BeautifulSoup

query = 'never gonna give you up'
search = requests.get('https://genius.com/api/search/?q={}'.format(query)).json()
url = search['response']['hits'][0]['result']['url']

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
    lyrics = tag.get_text(strip=True, separator='\n')

    if lyrics:
        print(lyrics) # do something with the lyrics
