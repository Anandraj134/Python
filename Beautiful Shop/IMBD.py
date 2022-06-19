import requests
import bs4

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
content = requests.get(url)
soup = bs4.BeautifulSoup(content.text, 'html.parser')
print(soup.find('title'))
for heading in soup.find_all('h1'):
    print(heading.text)
for heading in soup.find_all('h3'):
    print(heading.text)
