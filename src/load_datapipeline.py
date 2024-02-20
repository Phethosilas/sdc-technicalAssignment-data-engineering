import mysql.connector
import  datetime as dt
def save_articles_to_mysql(articles):
    """
    Saves articles to MySQL database.

    Args:
        articles (list): List of dictionaries containing article information.
    """
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="newsapi_schema"
    )
    cursor = conn.cursor()

    # Iterate over each article
    for article in articles:
        # Extract article data from dictionary
        source_name = article.get('source', {}).get('name', '')
        author = article.get('author', '')
        title = article.get('title', '')
        description = article.get('description', '')
        url = article.get('url', '')
        url_to_image = article.get('urlToImage', '')
        published_at = dt.datetime.strptime(article.get('publishedAt', ''),"%Y-%m-%dT%H:%M:%SZ").date()
        content = article.get('content', '')

        # Insert article into the articles table
        insert_query = """
            INSERT INTO articles 
            (source_name, author, title, description, url, url_to_image, published_at, content) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        article_data = (source_name, author, title, description, url, url_to_image, published_at, content)
        cursor.execute(insert_query, article_data)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()
