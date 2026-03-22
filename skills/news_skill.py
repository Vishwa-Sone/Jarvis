

import os
import requests
from logger import logger

# Keywords that trigger this skill
KEYWORDS = ["news", "headlines", "top news"]


def execute(command, speak, profile):
    """
    Fetches top headlines from NewsAPI.
    Uses news_country from user profile.
    """
    if "news" in command or "headlines" in command:
        try:
            newsapi      = os.getenv("NEWS_API_KEY")
            # Uses country from user profile — personalized!
            news_country = profile.get("news_country", "in")

            r = requests.get(
                f"https://newsapi.org/v2/top-headlines"
                f"?country={news_country}&apiKey={newsapi}"
            )

            if r.status_code == 200:
                data     = r.json()
                articles = data.get("articles", [])
                speak("Here are the top headlines Sir")
                for article in articles[:3]:
                    speak(article.get("title", "No title"))
                logger.info(f"Fetched {len(articles)} news articles.")
            else:
                logger.warning(f"News API status: {r.status_code}")
                speak("I encountered an issue fetching the news")

        except Exception as e:
            logger.error(f"News fetch error: {e}")
            speak("I am unable to connect to the news service")

        return True

    return False