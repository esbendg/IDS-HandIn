import requests
from newsapi import NewsApiClient


def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "859e740202ab4f9a8a8a187ea16101a3"
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
