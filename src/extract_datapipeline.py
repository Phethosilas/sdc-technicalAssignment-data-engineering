import requests


def get_news_articles(api_key, country='us'):
    """
    Fetches news articles from the NewsAPI.

    Args:
        api_key (str):  NewsAPI API key.
        country (str): The country code to filter articles by.

    Returns:
        list: A list containing dictionaries of articles.
    """
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'apiKey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data['articles']
    else:
        print(f"Error {response.status_code}: {data['message']}")
        return []
