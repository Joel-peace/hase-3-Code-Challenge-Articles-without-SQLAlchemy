def setup_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY(author_id) REFERENCES authors(id)
        );
    """)
    # Add other tables as needed
    
    conn.commit()
