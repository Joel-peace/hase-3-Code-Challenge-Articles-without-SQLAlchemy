class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self._id = id
        self.name = name  
        self.category = category  

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

    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if not value.strip():
            raise ValueError("Category must not be empty.")
        if hasattr(self, '_category') and self._category is not None:
            raise AttributeError("Category cannot be changed after instantiation.")
        self._category = value



    def create_magazine(self, cursor):
      
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self._name, self._category))
        self._id = cursor.lastrowid

    @classmethod
    def get_all_magazines(cls, cursor):
      
        cursor.execute("SELECT id, name, category FROM magazines")
        magazines_data = cursor.fetchall()
        return [cls(id=row[0], name=row[1], category=row[2]) for row in magazines_data]

    def articles(self, cursor):
        
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self._id,))
        return cursor.fetchall()

    def contributors(self, cursor):
       
        cursor.execute("""
            SELECT DISTINCT a.*
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self._id,))
        return cursor.fetchall()
