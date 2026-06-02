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
    You are 'Intelligence Daily', a premium AI curator. Your goal is to provide an easy-to-read briefing for a beginner.
    Today is {current_date}.
    
    NEWS DATA:
    {news_context}

    STRICT INSTRUCTIONS:
    1. FILTERING: Include ALL important news from the provided data. Do not limit yourself to major tech companies—cover anything interesting or impactful in tech, business, AI, and startups.
    2. QUANTITY: Include as many points as necessary. Do NOT cap it to 3-4 points. Group them logically under the headers.
    3. CONCISE BULLETS: Every bullet point MUST be a maximum of 1 or 2 short lines. Be incredibly brief and direct. Get straight to the point.
    4. EXPLAIN LIKE I'M 10: Use very basic, simple English. Absolutely NO corporate jargon, NO complex technical terms, and NO confusing acronyms. Write like you are explaining it to a middle-schooler.
    5. NO FLUFF: No "Hello," no introductory paragraphs. Start immediately with the headers.
    6. FORMATTING: Use EXACTLY the headers below starting with '##'. Each bullet must start with '* **Title:**' followed by the description.
    7. SOURCE: End every bullet with (Source: Name).

    STRUCTURE (MUST FOLLOW EXACTLY):
    
    ## EXECUTIVE SUMMARY
    * **The Big Picture:** (A 2-sentence ultra-simple overview of today's news.)

    ## 🚀 TOP UPDATES
    * **(Title):** (1-2 line simple explanation. (Source: Name))
    * (Add as many points as needed...)

    ## 🤖 AI & TECH NEWS
    * **(Title):** (1-2 line simple explanation. (Source: Name))
    * (Add as many points as needed...)

    ## 💼 BUSINESS & MARKETS
    * **(Title):** (1-2 line simple explanation. (Source: Name))
    * (Add as many points as needed...)

    ## 🧠 THE FINAL INTELLIGENCE
    * **Takeaway:** (One simple sentence on the future implication.)
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
