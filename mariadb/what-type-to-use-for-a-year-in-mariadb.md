# What type to use for a year in Mariadb?
// plain

The type to use for a year in Mariadb is `YEAR(4)`. This type is used to store a year in 4 digits format, such as 2020.

## Example code

```
CREATE TABLE mytable (
  year_column YEAR(4)
);
```

## Output example

```
Query OK, 0 rows affected (0.02 sec)
```

## Code explanation

- `CREATE TABLE`: This is a SQL command used to create a new table.
- `mytable`: This is the name of the table being created.
- `year_column`: This is the name of the column being created.
- `YEAR(4)`: This is the type of the column being created. It is used to store a year in 4 digits format.

## Helpful links
- [MySQL YEAR Type](https://dev.mysql.com/doc/refman/8.0/en/year.html)

onelinerhub: [What type to use for a year in Mariadb?](https://onelinerhub.com/mariadb/what-type-to-use-for-a-year-in-mariadb)