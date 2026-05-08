import feedparser
import datetime
import urllib.request

# Setting a User-Agent to pretend to be a browser (helps avoid being blocked)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def fetch_feed(url):
    try:
        # Use urllib to fetch the content with a custom User-Agent
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req) as response:
            content = response.read()
            return feedparser.parse(content)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

feed = fetch_feed("https://techcrunch.com/feed/")
if feed and feed.entries:
    entry = feed.entries[0]
    print(f"Title: {entry.title}")
    print(f"Published Parsed: {getattr(entry, 'published_parsed', 'N/A')}")
else:
    print("No entries found.")
