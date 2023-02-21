# coding: utf-8

import requests 
import urllib.parse
from bs4 import BeautifulSoup
import re

CHANNEL_NAME_PATTERN = "Uploaded\sBy:\s+(.*)\son.+"
UPLOADED_DATE_PATTERN = "Uploaded\sBy:.*on(.*)"
VIEWS_PATTERN = ":(.*)\sViews.*"

class YoutubeTrendItem:
    def __init__(self, title, url, channel_name, uploaded_date, volume):
        self.title = title
        self.url = url
        self.channel_name = channel_name
        self.uploaded_date = uploaded_date
        self.volume = volume
    
    def __repr__(self):
        return f"\n<YoutubeTrendItem title:{self.title} url:{self.url} channel_name:{self.channel_name} uploaded_date:{self.uploaded_date} volume:{self.volume}>"

if __name__ == "__main__":
    url = "https://yt-trends.iamrohit.in/Japan"

    items = []

    res = requests.get(url)
    if (res.status_code == 200):
        html_doc = res.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        elems = soup.select('.row.shadow-box > .col-md-8') 
        for elem in elems:
            a = elem.select_one('a.pl')
            title = a.text
            url = a.attrs['href']

            ps = elem.select('p')
            if (len(ps) > 0):
                channel_name_matches = re.findall(CHANNEL_NAME_PATTERN, ps[0].text)
                channel_name = channel_name_matches[0] if (len(channel_name_matches) > 0) else ""
                uploaded_date_matches = re.findall(UPLOADED_DATE_PATTERN, ps[0].text)
                uploaded_date = uploaded_date_matches[0] if (len(uploaded_date_matches) > 0) else ""
            if (len(ps) > 1):
                views_matches = re.findall(VIEWS_PATTERN, ps[1].text)
                views = views_matches[0] if (len(views_matches) > 0) else ""
            
            item = YoutubeTrendItem(title, url, channel_name, uploaded_date, views)
            items.append(item)

    print(items)


