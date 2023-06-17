# How do I use the PostgreSQL EXCEPT operator?
// plain

The PostgreSQL EXCEPT operator is used to compare the results of two SELECT statements and return any rows that are present in the first SELECT statement but not in the second SELECT statement. It is the equivalent of the MINUS operator in other database systems.

For example, the following code will return all rows from the ‘employee’ table that are not present in the ‘department’ table:

```
SELECT *
FROM employee
EXCEPT
SELECT *
FROM department;
```

The output of this query will depend on the data in the two tables.

## Code explanation


1. SELECT *: this is the command to select all columns from the table
2. FROM employee: this specifies the table to select from
3. EXCEPT: this is the EXCEPT operator
4. SELECT *: this is the command to select all columns from the table
5. FROM department: this specifies the table to select from

## Helpful links

- [PostgreSQL Documentation](https://www.postgresql.org/docs/9.4/sql-select.html)
- [EXCEPT Operator](https://www.postgresqltutorial.com/postgresql-except/)

onelinerhub: [How do I use the PostgreSQL EXCEPT operator?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-except-operator)