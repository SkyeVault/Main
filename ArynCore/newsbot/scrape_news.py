# scrape_news.py

from newspaper import Article
from bs4 import BeautifulSoup
import requests

APPROVED_SITES = [
    "https://www.npr.org",
    "https://www.bbc.com/news",
    "https://apnews.com",
    "https://www.reuters.com"
]

def extract_links(url):
    print(f"Scanning {url}")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return list(set(a['href'] for a in soup.find_all('a', href=True) if url in a['href']))

def extract_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "title": article.title,
            "text": article.text,
            "url": url
        }
    except Exception as e:
        print(f"[!] Failed to extract: {url}")
        return None

def run_scraper():
    collected = []
    for site in APPROVED_SITES:
        links = extract_links(site)
        for link in links[:5]:  # limit per site for now
            article_data = extract_article(link)
            if article_data:
                collected.append(article_data)
    return collected

if __name__ == "__main__":
    articles = run_scraper()
    print(f"\n[✓] Collected {len(articles)} articles")
    for a in articles:
        print(f"- {a['title']} ({a['url']})")
