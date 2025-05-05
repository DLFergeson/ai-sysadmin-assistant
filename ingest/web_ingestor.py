import requests
from bs4 import BeautifulSoup

def ingest_web_article(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return "\n".join(p.get_text() for p in paragraphs if len(p.get_text()) > 20)
    except Exception as e:
        return f"Error reading URL: {str(e)}"
