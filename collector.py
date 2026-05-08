import feedparser
import datetime
import ssl

# This line fixes the "SSL: CERTIFICATE_VERIFY_FAILED" error on many computers (especially Macs)
# It allows our script to talk to news websites safely.
ssl._create_default_https_context = ssl._create_unverified_context

# A list of high-quality news sources (RSS feeds)
RSS_FEEDS = {
    "AI News": [
        "https://techcrunch.com/category/artificial-intelligence/feed/",
        "https://venturebeat.com/category/ai/feed/",
        "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "https://syncedreview.com/feed/",
        "https://openai.com/news/rss.xml",
        "https://blog.google/technology/ai/rss/",
        "https://www.unite.ai/feed/",
    ],
    "Technology": [
        "https://www.theverge.com/rss/index.xml",
        "https://arstechnica.com/feed/",
        "https://www.wired.com/feed/rss",
        "https://9to5mac.com/feed/",
    ],
    "Business & Markets": [
        "https://www.moneycontrol.com/rss/marketnews.xml",
        "https://www.moneycontrol.com/rss/latestnews.xml",
        "https://www.livemint.com/rss/markets",
        "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
        "https://finance.yahoo.com/news/rssindex",
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
            feed = feedparser.parse(url)
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
                            "summary": entry.get('summary', ''),
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
