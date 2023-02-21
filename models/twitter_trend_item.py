class TwitterTrendItem:
    def __init__(self, title, url, volume):
        self.title = title
        self.url = url
        self.volume = volume
    
    def __repr__(self):
        return f"\n<TwitterTrendItem title:{self.title} url:{self.url} volume:{self.volume}>"