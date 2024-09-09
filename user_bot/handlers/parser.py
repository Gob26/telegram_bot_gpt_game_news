import requests
from bs4 import BeautifulSoup
import re

from link import url

link = url

match = re.search(r'(https?://ixbt\.games/[\w/-]+)', link)

if match:
    link = match.group()
    print(link)

    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find("article", class_=f"publication-container")

    if block:
        article_text = block.get_text(strip=True)
        print(article_text)
    else:
        print("Статья не найдена на странице.")
else:
    print("URL не соответствует ожидаемому формату.")