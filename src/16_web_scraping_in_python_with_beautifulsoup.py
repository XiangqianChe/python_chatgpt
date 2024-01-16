# Part 16: Web Scraping in Python with BeautifulSoup

# Install BeautifulSoup and requests: pip install beautifulsoup4 requests

# 1. Basic Web Scraping
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://example.com'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the HTML
    title = soup.title.text
    paragraphs = soup.find_all('p')

    # Print Results
    print("Web Scraping Results:")
    print("Title:", title)
    print("Paragraphs:")
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")

# 2. Scraping a Dynamic Website
# In this example, we'll scrape quotes from http://quotes.toscrape.com

url_quotes = 'http://quotes.toscrape.com'
response_quotes = requests.get(url_quotes)

if response_quotes.status_code == 200:
    soup_quotes = BeautifulSoup(response_quotes.text, 'html.parser')

    # Extract quotes and authors
    quotes = soup_quotes.find_all('span', class_='text')
    authors = soup_quotes.find_all('small', class_='author')

    # Print Results
    print("\nScraping a Dynamic Website Results:")
    for i in range(len(quotes)):
        print(f"Quote: {quotes[i].text}")
        print(f"Author: {authors[i].text}\n")
else:
    print(f"Failed to retrieve quotes page. Status Code: {response_quotes.status_code}")
