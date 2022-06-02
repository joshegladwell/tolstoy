import requests
from bs4 import BeautifulSoup

def extract_titles():
    # Set URL of the website with contents of each volume
    titles_url = 'http://tolstoy.ru/creativity/90-volume-collection-of-the-works/?arrFilter_pf%5BCATEGORY%5D%5B%5D=&set_filter=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80&set_filter=Y'

    # Scrape volume content info
    titles_response = requests.get(titles_url)
    titles_soup = BeautifulSoup(titles_response.content, "html.parser")

    # Organize info into a list
    titles_text = []
    for vol_title in titles_soup.find_all('li')[114:-9]:
        titles_text.append(vol_title.text.split())

    # Clean list into a dictionary
    titles = []
    vol_nums = []

    for t in titles_text:
        titles.append(" ".join(t[2:]))
        vol_nums.append(int(t[1]))

    # Return dictionary
    return dict(zip(vol_nums, titles))

def generate_urls():
    urls = []

    for i in (range(1,92)):
        if (i < 10):
            urls.append('http://tolstoy.ru/online/90/0' + str(i) + '/')
        else:
            urls.append('http://tolstoy.ru/online/90/' + str(i) + '/')

    return urls
