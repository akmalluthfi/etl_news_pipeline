import requests
from bs4 import BeautifulSoup
from newspaper import Article


def scrape():
    response = requests.get("https://www.liputan6.com/")
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