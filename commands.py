from enum import Enum

class Command(Enum):
    SCRAPE_TWITTER_TREND = 0
    SCRAPE_GOOGLE_TREND = 1
    SCRAPE_YOUTUBE_TREND = 2