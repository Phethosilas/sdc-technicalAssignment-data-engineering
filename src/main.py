import os
from dotenv import load_dotenv

# Importing functions from extract_datapipeline and load_datapipeline modules
from extract_datapipeline import get_news_articles
from load_datapipeline import save_articles_to_mysql

if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    # Load API key from .env file
    load_dotenv()
    api_key = os.environ.get('api')

    # List of European country codes
    country_codes = ['gb', 'de', 'fr', 'es', 'it', 'nl']

    # Iterate over each country code
    for country_code in country_codes:
        # Inform the user which country's articles are being fetched
        print(f"Fetching articles from {country_code.upper()}:")

        # Fetch articles from NewsAPI for the current country code
        articles = get_news_articles(api_key, country=country_code)

        # If articles are fetched, save them to MySQL database
        if articles:
            save_articles_to_mysql(articles)
            # Inform the user about the number of articles saved
            print(f"{len(articles)} articles saved to MySQL database.")
        else:
            print("No articles fetched.")  # Inform the user if no articles were fetched
