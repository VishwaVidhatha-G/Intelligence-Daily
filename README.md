# 🗞️ Intelligence Daily: AI-Powered News Automation

Intelligence Daily is a zero-cost, fully automated news briefing system. It curates high-impact technology and stock market news, synthesizes it using Gemini 2.0 AI into beginner-friendly language, and delivers a premium editorial-style email every morning at 9:00 AM IST.

![Portfolio Edition](https://img.shields.io/badge/Edition-Premium_Portfolio-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Python_%7C_Gemini_AI_%7C_GitHub_Actions-green)

---

## 💎 Key Features

- **🧠 Smart Curation:** Scans 170+ high-quality RSS feeds (TechCrunch, Moneycontrol, The Verge, etc.) daily.
- **👶 Beginner-First Intelligence:** Explains complex tech and financial shifts in simple "6-year-old" English.
- **📊 Deep Market Reasoning:** Provides the "Why" behind Indian Stock Market (Nifty/Sensex) movements with a holistic timeline.
- **🛡️ Strict Content Gatekeeping:** Automatically filters out lifestyle fluff, entertainment, and sales to keep you focused on what moves the needle.
- **✉️ Premium Design:** Delivers a minimalist, architectural card-based email design inspired by Claude and modern digital newspapers.
- **🤖 100% Automated:** Powered by GitHub Actions to run every morning without any manual intervention.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10
- **AI Engine:** Google Gemini 2.0 (Flash)
- **Data Source:** RSS Feeds via `feedparser`
- **Automation:** GitHub Actions
- **Security:** Environment Variables & GitHub Secrets

---

## 🚀 How It Works

1. **Collector:** A Python script visits a curated list of RSS feeds and filters for articles published in the last 24 hours.
2. **Summarizer:** The collected data is sent to the Gemini 2.0 model with a "Simple Teacher" persona that enforces fact-density and deep reasoning.
3. **Mailer:** A custom HTML/CSS engine converts the AI output into a premium architectural card-based design.
4. **Scheduler:** GitHub Actions triggers the entire pipeline every morning at 03:30 UTC (09:00 AM IST).

---

## 🚀 Easy 5-Minute Setup (For Beginners)

You don't need to be a coder to use this! Follow these steps to get your own daily briefing:

1. **Fork this Repo:** Click the **Fork** button at the top right of this page to create your own copy.
2. **Get your API Key:** Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and get a free Gemini API Key.
3. **Get your Email Password:**
   - Go to your Google Account Settings -> Security.
   - Enable 2-Step Verification.
   - Search for "App Passwords" and create one for "Mail". You will get a 16-character code.
4. **Add Secrets to GitHub:**
   - In **your forked repo**, go to **Settings** -> **Secrets and variables** -> **Actions**.
   - Click **New repository secret** and add these four:
     - `GEMINI_API_KEY`: (Your key from step 2)
     - `EMAIL_USER`: (Your Gmail address)
     - `EMAIL_PASS`: (The 16-character code from step 3)
     - `RECEIVER_EMAIL`: (Where you want to receive the news)
5. **Turn it On:**
   - Go to the **Actions** tab in your repo.
   - Click **Daily Intelligence Briefing** on the left.
   - Click **Run workflow** -> **Run workflow**.
   - **That's it!** You will now get an email every morning at 9:00 AM IST.

---

## ⚙️ Advanced Setup (For Developers)
(If you want to run this locally on your own machine)

1. **Clone the Repo:** `git clone https://github.com/your-username/intelligence-daily.git`
2. **Install Deps:** `pip install -r requirements.txt`
3. **Environment:** Create a `.env` file with your keys (see `.env.example`).
4. **Run:** `python main.py`

---

*Built with ❤️ by Vishwa Vidhatha*
