CREATE TABLE IF NOT EXISTS articles (
    article_id INT AUTO_INCREMENT PRIMARY KEY,
    source_name VARCHAR(255),
    author VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    url VARCHAR(1000),
    url_to_image VARCHAR(255),
    published_at DATE,
    content TEXT
);
