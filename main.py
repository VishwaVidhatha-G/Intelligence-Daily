import sys
import traceback
from collector import fetch_news
from summarizer import summarize_news
from mailer import send_email
from datetime import datetime

def run_pipeline():
    try:
        print(f"--- Starting News Automation Pipeline: {datetime.now().strftime('%Y-%m-%d %H:%M')} ---")
        
        # 1. Fetch
        print("Step 1: Collecting news from RSS feeds...")
        articles = fetch_news()
        
        if not articles:
            print("No new articles found in the last 24 hours. Pipeline stopped.")
            return

        # 2. Summarize
        print(f"Step 2: Summarizing {len(articles)} articles with Gemini AI...")
        briefing = summarize_news(articles)
        
        # 3. Email
        from datetime import timedelta
        yesterday = datetime.now() - timedelta(days=1)
        subject = f"Intelligence Daily - {yesterday.strftime('%b %d, %Y')}"
        print(f"Step 3: Sending the briefing for {yesterday.strftime('%b %d, %Y')}...")
        send_email(subject, briefing)
        
        print("--- Pipeline Completed Successfully! ---")
    except Exception as e:
        print("\n!!! CRITICAL PIPELINE FAILURE !!!")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        print("\nTraceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()
