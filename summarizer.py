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
    You are 'Intelligence Daily', a premium AI curator. Your goal is to provide a high-signal intelligence briefing focused ONLY on the most critical AI and technology developments.
    Today is {current_date}.
    
    NEWS DATA:
    {news_context}

    STRICT INSTRUCTIONS:
    1. FILTERING: Ignore low-impact news, minor product tweaks, or niche updates. Focus exclusively on major AI model releases, significant developer tooling, major company shifts (OpenAI, Anthropic, Google, Microsoft, Meta), and massive ecosystem developments.
    2. TONE: Professional, highly analytical, and high-signal. Do NOT use "explain like I'm 10". Use precise, accurate terminology.
    3. DEEP DIVES (CRITICAL): Select exactly 3 to 5 of the absolute most important stories of the day. For each, write a comprehensive 3-4 sentence analytical paragraph explaining what happened and why it matters.
    4. QUICK HITS: Select exactly 4 to 6 "Other Important Updates". These must be strictly 1-line bullet points.
    5. NO FLUFF: No introductory greetings. No conversational filler.
    6. FORMATTING: Use EXACTLY the headers below starting with '##'.
    7. SOURCE: End every story with (Source: Name).

    STRUCTURE (MUST FOLLOW EXACTLY):
    
    ## 🏆 TOP STORIES OF THE DAY
    * **(Title)**
      (3-4 sentence comprehensive analytical paragraph. (Source: Name))
      
    * **(Title)**
      (3-4 sentence comprehensive analytical paragraph. (Source: Name))
      
    * (Add 1-3 more deep dives following the exact format above)

    ## ⚡ WHAT ELSE IS HAPPENING
    * **(Title):** (1-line simple explanation. (Source: Name))
    * **(Title):** (1-line simple explanation. (Source: Name))
    * (Add 2-4 more quick hits following the exact format above)
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
