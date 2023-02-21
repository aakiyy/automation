class GoogleTrendItem:
    def __init__(self, title, url, volume):
        self.title = title
        self.url = url
        self.volume = volume
    
    def __repr__(self):
        return f"<GoogleTrendItem title:{self.title} url:{self.url} volume:{self.volume}>"