# How do I use the SQLite VARCHAR data type?
// plain

The SQLite VARCHAR data type is used to store variable-length character strings. It can store up to 1,073,741,824 characters. To use it, you must specify the maximum size of the string you want to store when you create the table. For example:

```sql
CREATE TABLE contacts (
  name VARCHAR(50)
);
```

This will create a table called `contacts` with a column called `name` that can store up to 50 characters.

You can then insert values into the table like this:

```sql
INSERT INTO contacts (name) VALUES ('John');
```

You can also use the `VARCHAR` data type in `SELECT` statements. For example:

```sql
SELECT name FROM contacts WHERE name LIKE 'J%';
```

This will return all names from the `contacts` table that start with the letter `J`.

You can also use the `VARCHAR` data type in `UPDATE` statements. For example:

```sql
UPDATE contacts SET name = 'Jane' WHERE name = 'John';
```

This will update the `name` column for all rows where the name is `John` to `Jane`.

## Helpful links
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite VARCHAR Data Type](https://www.sqlitetutorial.net/sqlite-data-types/#varchar)

onelinerhub: [How do I use the SQLite VARCHAR data type?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-varchar-data-type)