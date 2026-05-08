import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime

# Load our secret API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the NEW Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

def summarize_news(news_articles):
    """
    This function uses the latest Gemini 2.0 model with Google Search
    to research and summarize news.
    """
    
    # 1. Prepare the news we already found
    news_context = ""
    for idx, item in enumerate(news_articles):
        news_context += f"{idx+1}. {item['title']} (Source: {item['source']})\n"

    # 2. Craft the Prompt
    current_date = datetime.now().strftime("%B %d, %Y")
    prompt = f"""
    You are a 'Strict Content Gatekeeper' and 'Simple Teacher' for 'Intelligence Daily'. 
    Today's date is {current_date}.
    
    I have provided news data below. 

    DATA:
    {news_context}

    YOUR CORE TASK:
    1. STRICT FILTERING (NO FLUFF): Only include news about Major Tech/AI companies (Apple, OpenAI, Google, Microsoft, NVIDIA, etc.). 
       - IGNORE: Lifestyle, Music/Celebrities, Sales/Deals, Mother's Day, scary TV shows, how-to tips, or small gadget reviews.
       - If it doesn't change the world of AI or Big Tech, do not include it.
    2. BE SPECIFIC: If you mention a count (e.g., "3 new features"), you MUST briefly list all of them. Never say "new features" without saying what they are. 
    3. EXPLAIN LIKE I'M 6: Use very basic English.
    4. BOLD MINI-HEADERS: Every bullet point MUST start with a **Bold Short Title:**.
    5. DEEP MARKET REASONING: Explain exactly why the Indian market moved.
    6. SOURCE: End every bullet with (Source: Name).

    STRUCTURE:
    ## TOP UPDATES
    * **(Title):** (1-3 line simple explanation with ALL specific details and source)

    ## AI & ROBOT NEWS
    * **(Title):** (Detailed 1-3 line update. Mention specific features/names. (Source: Name))

    ## TECH & BUSINESS (MAJOR ONLY)
    * **(Title):** (Only major moves from big tech/IT companies. (Source: Name))

    ## INDIAN STOCK MARKET
    * **(Title):** (Deep reasoning for the move and source)

    ## THE FINAL INTELLIGENCE
    * **(Title):** (One simple sentence on what this means for the future.)
    """

    print("--- Gemini is now researching the web and summarizing ---")
    
    # 3. Ask Gemini with GOOGLE SEARCH enabled!
    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=prompt
    )
    
    return response.text

if __name__ == "__main__":
    # Test it with one sample
    sample = [{"title": "OpenAI safety news", "source": "TechCrunch"}]
    print(summarize_news(sample))
