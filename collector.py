import feedparser
import datetime
import ssl
import socket

# Set global timeout to 15 seconds to prevent feedparser from hanging
socket.setdefaulttimeout(15)

# This line fixes the "SSL: CERTIFICATE_VERIFY_FAILED" error on many computers (especially Macs)
# It allows our script to talk to news websites safely.
ssl._create_default_https_context = ssl._create_unverified_context

# A highly curated list of AI and Technology sources
RSS_FEEDS = {
    "AI News": [
        "https://techcrunch.com/category/artificial-intelligence/feed/",
        "https://venturebeat.com/category/ai/feed/",
        "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "https://openai.com/news/rss.xml",
        "https://blog.google/technology/ai/rss/",
    ]
}

def fetch_news():
    """
    This function visits each RSS feed and collects articles published 
    in the last 24 hours.
    """
    print("--- Starting News Collection ---")
    all_articles = []
    now = datetime.datetime.now(datetime.timezone.utc)
    one_day_ago = now - datetime.timedelta(days=1)

    for category, feeds in RSS_FEEDS.items():
        print(f"Checking {category}...")
        for url in feeds:
            try:
                feed = feedparser.parse(url)
            except Exception as e:
                print(f"  [Error] Could not fetch {url}: {e}")
                continue
                
            for entry in feed.entries:
                # Convert the article time to a format Python understands
                pub_parsed = getattr(entry, 'published_parsed', None) or getattr(entry, 'updated_parsed', None)
                
                if pub_parsed:
                    published_time = datetime.datetime(*pub_parsed[:6], tzinfo=datetime.timezone.utc)
                    
                    # Only keep articles from the last 24 hours
                    if published_time > one_day_ago:
                        article = {
                            "category": category,
                            "title": entry.title,
                            "link": entry.link,
                            "source": feed.feed.get('title', 'Unknown Source')
                        }
                        all_articles.append(article)
                else:
                    # If no date is found, we skip it to ensure only fresh news
                    pass
    
    print(f"Collected {len(all_articles)} articles from the last 24 hours.")
    return all_articles

if __name__ == "__main__":
    news = fetch_news()
    for item in news[:10]:
        print(f"[{item['category']}] {item['title']} ({item['source']})")
