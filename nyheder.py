import requests
<<<<<<< HEAD
import pygame
from newsapi import NewsApiClient

=======

from newsapi import NewsApiClient


>>>>>>> 3cd0322d7160c5e0094ae8241f0206a95c4a8335
def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "fe8271c563c049a0948a2071ed7ff98e"
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    print (open_bbc_page)
    article = open_bbc_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    #for i in range(len(results)):
    #    i + 1, results[i]
    return results


if __name__ == '__main__':
    NEWS_DATA = NewsFromBBC()
