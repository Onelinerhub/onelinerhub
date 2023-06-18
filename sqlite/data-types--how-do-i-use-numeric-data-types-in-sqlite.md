# data types

How do I use numeric data types in SQLite?
// plain

SQLite is a relational database management system which supports numeric data types. It supports several types of numeric data types such as INTEGER, REAL, and NUMERIC. These data types can be used to store numeric values such as integers, floating-point numbers, and decimals.

For example, the following code creates a table called 'table1' with an INTEGER column called 'num1':
```
CREATE TABLE table1 (
    num1 INTEGER
);
```

The INTEGER data type is used to store integers such as whole numbers and negative numbers. The REAL data type is used to store floating-point numbers such as 3.1415. The NUMERIC data type is used to store decimals such as 0.123.

The following code inserts a row into the table with the value of 5 for the column 'num1':
```
INSERT INTO table1 (num1) VALUES (5);
```

The following code selects the value of 'num1' from the table:
```
SELECT num1 FROM table1;

## Output example

5
```

## Code explanation


1. CREATE TABLE table1 (num1 INTEGER): This statement creates a table called 'table1' with an INTEGER column called 'num1'.
2. INSERT INTO table1 (num1) VALUES (5): This statement inserts a row into the table with the value of 5 for the column 'num1'.
3. SELECT num1 FROM table1: This statement selects the value of 'num1' from the table.

## Helpful links

- SQLite Data Types: https://www.sqlite.org/datatype3.html
- SQLite CREATE TABLE: https://www.sqlitetutorial.net/sqlite-create-table/
- SQLite INSERT INTO: https://www.sqlitetutorial.net/sqlite-insert/
- SQLite SELECT: https://www.sqlitetutorial.net/sqlite-select/

onelinerhub: [data types

How do I use numeric data types in SQLite?](https://onelinerhub.com/sqlite/data-types--how-do-i-use-numeric-data-types-in-sqlite)