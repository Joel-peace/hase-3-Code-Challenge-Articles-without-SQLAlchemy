class Author:
    def __init__(self, id=None, name=None):
        self._id = id
        self.name = name 

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name must not be empty.")
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Name cannot be changed after instantiation.")
        self._name = value

    def create_author(self, cursor):
        """Insert this author into the database."""
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
        self._id = cursor.lastrowid

    @classmethod
    def get_all_authors(cls, cursor):
        """Fetch all authors from the database."""
        cursor.execute("SELECT id, name FROM authors")
        authors_data = cursor.fetchall()
        return [cls(id=row[0], name=row[1]) for row in authors_data]

    def articles(self, cursor):
        """Get all articles written by this author."""
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        return cursor.fetchall()

    def magazines(self, cursor):
        """Get all magazines linked to this author's articles."""
        cursor.execute("""
            SELECT DISTINCT m.*
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self._id,))
        return cursor.fetchall()
