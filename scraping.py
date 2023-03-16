import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Wikipedia'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# find all links on the page
links = soup.find_all('a')

# find all images on the page
images = soup.find_all('img')

# extract the href attribute from all links on the page
hrefs = [link.get('href') for link in links]

# extract the src attribute from all images on the page
srcs = [img.get('src') for img in images]


print(len(hrefs))