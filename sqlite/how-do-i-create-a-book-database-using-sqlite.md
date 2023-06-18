# How do I create a book database using SQLite?
// plain

Creating a book database using SQLite is simple. First, you need to create a table to store your book data. The example below creates a table called `books` with four fields: `title`, `author`, `year` and `price`:

```
CREATE TABLE books (
    title TEXT,
    author TEXT,
    year INTEGER,
    price REAL
);
```

Then, you can insert books into the table using the `INSERT` statement. The following example inserts a book with title 'The Catcher in the Rye', author 'J.D. Salinger', published in 1951 and a price of 10.99:

```
INSERT INTO books (title, author, year, price)
VALUES ('The Catcher in the Rye', 'J.D. Salinger', 1951, 10.99);
```

You can also query the table to get information about the books. For example, the following query retrieves all books written by J.D. Salinger:

```
SELECT title, year, price
FROM books
WHERE author = 'J.D. Salinger';
```

The output of this query would be:

```
title		year	price
The Catcher in the Rye	1951	10.99
```

Finally, you can also delete books from the table using the `DELETE` statement. For example, the following statement deletes the book 'The Catcher in the Rye' from the table:

```
DELETE FROM books
WHERE title = 'The Catcher in the Rye';
```

For more information about SQLite, please refer to the [SQLite documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How do I create a book database using SQLite?](https://onelinerhub.com/sqlite/how-do-i-create-a-book-database-using-sqlite)