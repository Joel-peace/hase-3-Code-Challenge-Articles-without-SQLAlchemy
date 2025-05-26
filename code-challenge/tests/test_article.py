import sqlite3
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article  # adjust import paths accordingly

def setup_db(cursor):
    cursor.execute("""
    CREATE TABLE authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY(author_id) REFERENCES authors(id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
    )
    """)

def test_article():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_db(cursor)

   
    author = Author(name="Alice")
    author.create_author(cursor)


    magazine = Magazine(name="Science Monthly", category="Science")
    magazine.create_magazine(cursor)

    conn.commit()

    article = Article(title="The Wonders of Space", author_id=author.id, magazine_id=magazine.id)
    article.create_article(cursor)
    conn.commit()

    print(f"Created article with id={article.id}, title={article.title}, author_id={article.author_id}, magazine_id={article.magazine_id}")


    articles = Article.get_all_articles(cursor)
    print("Articles in DB:")
    for a in articles:
        print(f"id={a.id}, title={a.title}, author_id={a.author_id}, magazine_id={a.magazine_id}")

    conn.close()

if __name__ == "__main__":
    test_article()
