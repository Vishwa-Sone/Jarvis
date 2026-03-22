

import webbrowser
from logger import logger

# Keywords that trigger this skill
KEYWORDS = ["open google", "open youtube", "open linkedin"]

# Website mapping
SITES = {
    "google":   "https://google.com",
    "youtube":  "https://youtube.com",
    "linkedin": "https://linkedin.com"
}


def execute(command, speak, profile):
    """
    Opens the requested website in the browser.
    """
    for site, url in SITES.items():
        if site in command:
            speak(f"Opening {site.capitalize()}")
            webbrowser.open(url)
            logger.info(f"Opened website: {url}")
            return True

    return False