-- ~~~~sql
IF OBJECT_ID('authors', 'U') IS NOT NULL DROP TABLE authors;
CREATE TABLE authors (
	id INT IDENTITY(1,1) PRIMARY KEY,
	name NVARCHAR(255) NOT NULL
);

IF OBJECT_ID('magazines', 'U') IS NOT NULL DROP TABLE magazines;
CREATE TABLE magazines (
	id INT IDENTITY(1,1) PRIMARY KEY,
	name NVARCHAR(255) NOT NULL,
	category NVARCHAR(255) NOT NULL
);

IF OBJECT_ID('articles', 'U') IS NOT NULL DROP TABLE articles;
CREATE TABLE articles (
	id INT IDENTITY(1,1) PRIMARY KEY,
	title NVARCHAR(255) NOT NULL,
	author_id INT,
	magazine_id INT,
	FOREIGN KEY (author_id) REFERENCES authors(id),
	FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);