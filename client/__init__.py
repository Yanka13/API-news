# client/__init__.py
import requests
import os


class News:
    API_KEY = os.environ['API_KEY']
    BASE_URL = "https://newsapi.org/v2"
    def search(self, keyword):
        url = f"{self.BASE_URL}/everything?"
        params = {"q": keyword, "apiKey": self.API_KEY}
        request = requests.get(url, params=params)
        response = request.json()
        articles = response["articles"]
        return articles

    def top_headlines(self, country):
        url = f"{self.BASE_URL}/top-headlines?"
        params = {"country": country, "apiKey":  self.API_KEY}
        request = requests.get(url, params=params)
        response = request.json()
        articles = response["articles"]
        return articles


if __name__ == "__main__":
    news = News()
    print(news.BASE_URL)
    print(news.search("TDD"))
