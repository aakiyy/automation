# coding: utf-8

import requests 
import urllib.parse
from bs4 import BeautifulSoup
from models.google_trend_item import GoogleTrendItem

class GoogleTrendService:
    def scrape_google_trends():
        url = "https://gtrends.iamrohit.in/Japan"

        items = []

        res = requests.get(url)
        if (res.status_code == 200):
            html_doc = res.text
            soup = BeautifulSoup(html_doc, 'html.parser')
            elems = soup.select('.row.shadow-box > .col-md-9') 
            for elem in elems:
                title = elem.select_one('strong').text.strip().strip(":")
                url = "https://www.google.com/search?q=" + urllib.parse.quote(title)
                volume = elem.select_one('span.badge').text.strip().strip(" Searches")
                item = GoogleTrendItem(title, url, volume)
                items.append(item)

        print(items)