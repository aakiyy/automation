# coding: utf-8

import requests 
from bs4 import BeautifulSoup
from models.twitter_trend_item import TwitterTrendItem

class TwitterTrendService:
    def scrape_twitter_trends():
        url = "https://twitter-trends.iamrohit.in/japan"

        items = []

        res = requests.get(url)
        if (res.status_code == 200):
            html_doc = res.text
            soup = BeautifulSoup(html_doc, 'html.parser')
            elems = soup.select('#copyData > tr') 
            for elem in elems:
                a = elem.select_one('th > a.tweet')
                if (a is None): continue

                title = a.text
                url = a.attrs['href']
                volume = a.attrs['tweetcount']
                
                item = TwitterTrendItem(title, url, volume)
                items.append(item)

        print(items)