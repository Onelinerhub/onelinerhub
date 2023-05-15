# Mariadb fulltext search example
// plain

Mariadb fulltext search is a powerful search feature that allows you to search for words and phrases within a database. Here is an example of how to use it:

```
CREATE TABLE articles (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  body TEXT NOT NULL,
  FULLTEXT (title,body)
);

INSERT INTO articles (title, body) VALUES
  ('How to use Mariadb fulltext search', 'Mariadb fulltext search is a powerful search feature that allows you to search for words and phrases within a database.');

SELECT * FROM articles
  WHERE MATCH (title,body) AGAINST ('Mariadb fulltext search');
```

## Output example

```
id  title                                            body
1   How to use Mariadb fulltext search               Mariadb fulltext search is a powerful search feature that allows you to search for words and phrases within a database.
```

The example code above creates a table called `articles` with two columns, `title` and `body`. The `FULLTEXT` keyword is used to create a fulltext index on the `title` and `body` columns. Then, an article is inserted into the table. Finally, a query is executed to search for the phrase `Mariadb fulltext search` in the `title` and `body` columns. The output of the query is the article that was inserted.

## Code explanation

- `CREATE TABLE articles`: creates a table called `articles` with two columns, `title` and `body`.
- `FULLTEXT (title,body)`: creates a fulltext index on the `title` and `body` columns.
- `INSERT INTO articles`: inserts an article into the table.
- `SELECT * FROM articles`: executes a query to search for the phrase `Mariadb fulltext search` in the `title` and `body` columns.

## Helpful links
- [Mariadb Fulltext Search Documentation](https://mariadb.com/kb/en/library/fulltext-search/)

onelinerhub: [Mariadb fulltext search example](https://onelinerhub.com/mariadb/mariadb-fulltext-search-example)