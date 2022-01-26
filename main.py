# main.py
from client import News


def main():
    news = News()
    choice = input("Country headlines [default] or Search [hit s]?")
    if choice == "s":
        keyword = input("What are you looking for?")
        articles = news.search(keyword)
        for article in articles:
            print(f" - {article['title']}")
    else:
        articles = news.top_headlines("fr")
        for article in articles:
            print(f" - {article['title']}")


if __name__ == '__main__':
    main()
