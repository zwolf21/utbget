import re
import requests

from bs4 import BeautifulSoup

def get_search_results(keywords, n=10):
    url = "https://youtube.com/results"
    params = {
        'search_query': keywords
    }
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    regex = re.compile(r'/watch\?v=(?P<content_id>.+)')
    ret = []
    for link in soup('a', href=regex, class_='yt-uix-tile-link'):
        title = link.text.strip()
        href = link['href']
        m = regex.search(href).group
        content_id = m('content_id')
        row = dict(
            title=title,
            link=f"https://youtu.be/{content_id}"
        )
        ret.append(row)
    return ret[:n]
