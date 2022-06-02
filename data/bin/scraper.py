import requests
from bs4 import BeautifulSoup
import re

# Create volume object
class Volume:
    def __init__(self, volnum, text, tokens):
        self.text = text
        self.tokens = tokens
        self.volnum = volnum

# Scraper function
# TODO: Clean up the commentary and index in the texts
# TODO: Eventually aggregate by sections/chapters
def tolstoy_scraper(url):
    # Get url of the volume
    response = requests.get(url)
    
    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    
    # Extract all words using regexes
    words = re.findall('\w+', text)

    # Put all words into lowercase
    lowered = []
    for word in words:
        lowered.append(word.lower())
       
    # Replace all whitespace (\n, \t, " ", "  ", etc) with " "
    clean_text = " ".join(text.split())
    
    # Return the given Volume object
    output_vol = Volume(int(url[-3:-1]), clean_text, lowered)
    return output_vol