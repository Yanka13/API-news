import unittest

from client import News
# une methode search(keyword) -> /everything
# une methode top_headlines(country) -> /top-headlines

class NewsTest(unittest.TestCase):
    # un premier test pour tester notre methode search
    def test_search(self):
        # créer une instance de la classe News
        news = News()

        articles = news.search('madagascar')

        #Assertion
        # il faut vérifier que la fonction marche :
        # qu'on récupère bien des articles !
        # -> vérifier qu'on en récupère au moins 1
        #len(articles) > 0
        self.assertGreater(len(articles), 0)
        # -> vérifier qu'on répurère une liste
        self.assertEqual(type(articles), list)



    # un second test pour tester la méthode top_headlines
    def test_headlines(self):
        # créer une instance de la classe News
        news = News()

        articles = news.top_headlines('us')

        #Assertion
        # il faut vérifier que la fonction marche :
        # qu'on récupère bien des articles !
        # -> vérifier qu'on en récupère au moins 1
        #len(articles) > 0
        self.assertGreater(len(articles), 0)
        # -> vérifier qu'on répurère une liste
        self.assertEqual(type(articles), list)
