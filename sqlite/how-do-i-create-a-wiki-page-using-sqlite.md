# How do I create a Wiki page using SQLite?
// plain

Creating a Wiki page using SQLite is a simple process that involves creating a database and then creating a table in that database. To start, you need to install SQLite on your computer and then open a terminal window.

From the terminal window, run the command `sqlite3 wiki.db` to create a database named ‘wiki.db’.

Once the database is created, you can create a table in it by running the command `CREATE TABLE wiki (id INTEGER PRIMARY KEY, title TEXT, content TEXT);`. This will create a table named ‘wiki’ with three columns – id, title, and content.

You can then insert data into the table by running the command `INSERT INTO wiki (title, content) VALUES ('My First Wiki Page', 'This is the content of my first wiki page.');`. This will insert a row into the table with the title ‘My First Wiki Page’ and the content ‘This is the content of my first wiki page.’

Once you have inserted the data into the table, you can view it by running the command `SELECT * FROM wiki;`. This will display the contents of the table, including the title and content of the Wiki page.

To view the Wiki page, you can run the command `SELECT content FROM wiki WHERE title='My First Wiki Page';`. This will display the content of the Wiki page.

You can also update the content of the Wiki page by running the command `UPDATE wiki SET content='This is the updated content of my first wiki page.' WHERE title='My First Wiki Page';`. This will update the content of the Wiki page with the new content.

## Helpful links
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/index.htm)

onelinerhub: [How do I create a Wiki page using SQLite?](https://onelinerhub.com/sqlite/how-do-i-create-a-wiki-page-using-sqlite)