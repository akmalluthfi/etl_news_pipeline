import requests
from bs4 import BeautifulSoup
from newspaper import Article


def scrape():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Encoding": "gzip",
        "Connection": "keep-alive",
    }
    response = requests.get("https://www.liputan6.com/", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a", class_="breaking-news__click")
    url = link.get("href")

    article = Article(url)
    article.download()
    article.parse()

    text = article.text
    text_cleaned = text.replace("\n", " ").strip()

    return {
        "author": article.authors[0],
        "published_at": article.publish_date.strftime("%Y-%m-%d"),
        "text": text_cleaned,
    }
