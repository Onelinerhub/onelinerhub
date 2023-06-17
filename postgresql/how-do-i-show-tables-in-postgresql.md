# How do I show tables in PostgreSQL?
// plain

To show tables in PostgreSQL, you can use the command `\d` or `\dt` in the psql command line.

## Example code

```
\d
```

## Output example

```
                 List of relations
 Schema |         Name         | Type  |  Owner
--------+---------------------+-------+---------
 public | customers            | table | postgres
 public | orders               | table | postgres
 public | products             | table | postgres
(3 rows)
```

The command `\d` will show all the tables, views, sequences, and foreign tables in the current database. The command `\dt` will only show the tables.

Parts of the code:
- `\d` or `\dt`: These are the commands used to show the tables in PostgreSQL.
- `public`: This is the schema of the database.
- `customers`, `orders`, `products`: These are the names of the tables.
- `table`: This is the type of the object.
- `postgres`: This is the owner of the table.

## Helpful links
- https://www.postgresql.org/docs/9.1/sql-syntax-lexical.html
- https://www.postgresql.org/docs/9.1/sql-commands.html

onelinerhub: [How do I show tables in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-show-tables-in-postgresql)