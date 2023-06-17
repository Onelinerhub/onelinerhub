# statement

How do I use the PostgreSQL LIKE statement?
// plain

The PostgreSQL LIKE statement is used to match text values against patterns using wildcards. It is commonly used to search for specific patterns within a string of text.

For example, the following statement will match any string that contains the word “dog”:

```
SELECT * FROM table_name WHERE column_name LIKE '%dog%';
```

The output of this statement will be any row that contains the word “dog” in the specified column.

The wildcards used in the LIKE statement are:

* % - Matches any number of characters
* _ - Matches any single character

For example, the following statement will match any string that starts with “dog”:

```
SELECT * FROM table_name WHERE column_name LIKE 'dog%';
```

The output of this statement will be any row that starts with the word “dog” in the specified column.

The LIKE statement can also be used with the NOT operator to exclude certain patterns from the results. For example, the following statement will match any string that does not contain the word “dog”:

```
SELECT * FROM table_name WHERE column_name NOT LIKE '%dog%';
```

The output of this statement will be any row that does not contain the word “dog” in the specified column.

For more information about the PostgreSQL LIKE statement, please refer to the following links:

* [PostgreSQL Documentation: LIKE](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-LIKE)
* [PostgreSQL Tutorial: LIKE Clause](https://www.postgresqltutorial.com/postgresql-like/)

onelinerhub: [statement

How do I use the PostgreSQL LIKE statement?](https://onelinerhub.com/postgresql/statement--how-do-i-use-the-postgresql-like-statement)