import nltk
import re
import pandas as pd

# Import scraper function
import scraper

# Read in volume content information
import corpus_info
title_dict = corpus_info.extract_titles()
urls = corpus_info.generate_urls()

# Cycle through URLs to scrape text
volumes = []
for url in urls: # use urls[:45] for publications only
    vol = scraper.tolstoy_scraper(url)
    
    volumes.append([vol.volnum, title_dict[vol.volnum], vol.text, vol.tokens])

# Create dataframe
cols = ['volume', 'title', 'text', 'text_tokenized'] # TODO: add volume type and years
corpus_df = pd.DataFrame(volumes, columns=cols)

# Export as csv
corpus_df.to_csv('data/tolstoy_corpus.csv', index=False)
