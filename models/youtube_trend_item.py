class YoutubeTrendItem:
    def __init__(self, title, url, channel_name, uploaded_date, volume):
        self.title = title
        self.url = url
        self.channel_name = channel_name
        self.uploaded_date = uploaded_date
        self.volume = volume
    
    def __repr__(self):
        return f"\n<YoutubeTrendItem title:{self.title} url:{self.url} channel_name:{self.channel_name} uploaded_date:{self.uploaded_date} volume:{self.volume}>"