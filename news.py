import requests

# This function gets the headlines from the BBC news through the news api. 
def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "1d29f9ebc84a46a7b0a5441de94b3d78"
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    # print (open_bbc_page)
    article = open_bbc_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    #for i in range(len(results)):
    #    i + 1, results[i]
    return results


if __name__ == '__main__':
    NEWS_DATA = NewsFromBBC()
