class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self._id = id
        self.title = title  
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string.")
        if not value.strip():
            raise ValueError("Title must not be empty.")
        self._title = value

    def create_article(self, cursor):
        """Insert this article into the database."""
        if self.author_id is None or self.magazine_id is None:
            raise ValueError("Author ID and Magazine ID must be set before creating an article.")
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (self._title, self.author_id, self.magazine_id)
        )
        self._id = cursor.lastrowid

    @classmethod
    def get_all_articles(cls, cursor):
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles")
        articles_data = cursor.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in articles_data]