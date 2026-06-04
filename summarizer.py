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
    You are 'Intelligence Daily', a premium AI curator. Your goal is to provide a high-signal intelligence briefing covering every meaningful development.
    Today is {current_date}.
    
    NEWS DATA:
    {news_context}

    STRICT INSTRUCTIONS:
    1. ZERO INFORMATION LOSS: You must summarize EVERY single unique and meaningful story from the provided data. Do not skip any important developments.
    2. TONE: Professional, highly analytical, and high-signal. Use precise terminology.
    3. CONCISE BULLET POINTS: Every single story MUST be summarized in exactly 1 to 2 lines. Do NOT write long paragraphs. Keep it punchy and incredibly dense with facts.
    4. NO FLUFF: No introductory greetings. No conversational filler.
    5. FORMATTING: Use EXACTLY the headers below starting with '##'. Each bullet must start with '* **Title:**' followed by the description.
    6. SOURCE: End every story with (Source: Name).

    STRUCTURE (MUST FOLLOW EXACTLY):
    
    ## 🚀 TOP UPDATES
    * **(Title):** (1-2 line concise, fact-dense explanation. (Source: Name))
    * (Add as many points as needed to capture everything)

    ## 🤖 AI & TECH NEWS
    * **(Title):** (1-2 line concise, fact-dense explanation. (Source: Name))
    * (Add as many points as needed to capture everything)
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
