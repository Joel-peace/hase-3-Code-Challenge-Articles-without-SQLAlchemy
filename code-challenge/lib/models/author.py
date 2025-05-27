import sqlite3
import pytest
from lib.models.author import Author

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
        name TEXT NOT NULL
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

def test_create_author():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_db(cursor)

    author = Author(name="John")
    author.create_author(cursor)
    conn.commit()

    assert author.id is not None
    assert author.name == "John"

    conn.close()

def test_create_author_jane():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_db(cursor)

    author = Author(name="Jane")
    author.create_author(cursor)
    conn.commit()

    assert author.id is not None
    assert author.name == "Jane"

    conn.close()

def test_get_all_authors_with_john_and_jane():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_db(cursor)

    author1 = Author(name="John")
    author1.create_author(cursor)

    author2 = Author(name="Jane")
    author2.create_author(cursor)

    conn.commit()

    authors = Author.get_all_authors(cursor)
    names = [a.name for a in authors]

    assert "John" in names
    assert "Jane" in names

    conn.close()

def test_articles_for_john_empty():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_db(cursor)

    author = Author(name="John")
    author.create_author(cursor)
    conn.commit()

    articles = author.articles(cursor)
    assert articles == []

    conn.close()

def test_multiple_authors_count():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_db(cursor)

    names = ["John", "Jane", "John", "Jane"]
    for name in names:
        author = Author(name=name)
        author.create_author(cursor)

    conn.commit()
    conn.close()
