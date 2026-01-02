import requests

import selectorlib
# Imports the requests and the sectorlib library

URL = "https://programmer100.pythonanywhere.com/tours/" # Stores the url in a variable named URL.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
def scrape(url):# defines the function.
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)# gets the URL.
    source = response.text # Shows the page source.
    return source # returns the page source.

def extract(source):# defines another function.
    """Extract the data from the source page"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml") # extracts the data from extract.yaml.
    value = extractor.extract(source)["tours"] # extract the tours part from the source
    return value # returns the tours.

if __name__ == "__main__": # runs the program when the script is executed only in main.py.
    scraped = scrape(url=URL) # scrapes the page source.
    extracted = extract(scraped) # extracts tours from the URL.
    print(extracted) # prints tours.