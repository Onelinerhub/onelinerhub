# How do I use SQLite xfilter to filter data?
// plain

SQLite xfilter is a powerful tool for filtering data. It allows you to specify a condition to filter the data. To use it, you first need to specify the column you want to filter on, followed by the condition you want to filter on. For example, to filter a table called 'customers' for customers with an age greater than 30, the following SQL query can be used:

```
SELECT * FROM customers WHERE age > 30
```

The output of this query would be a list of customers with an age greater than 30.

The xfilter can also be used to filter data based on multiple conditions. For example, to filter customers with an age greater than 30 and a last name that starts with 'S':

```
SELECT * FROM customers WHERE age > 30 AND last_name LIKE 'S%'
```

The output of this query would be a list of customers with an age greater than 30 and a last name that starts with 'S'.

The xfilter can also be used to filter data based on a range of values. For example, to filter customers with an age between 18 and 25:

```
SELECT * FROM customers WHERE age BETWEEN 18 AND 25
```

The output of this query would be a list of customers with an age between 18 and 25.

## Helpful links

- [SQLite xfilter Documentation](https://www.sqlite.org/xfilter.html)
- [SQLite WHERE Clause Documentation](https://www.sqlite.org/lang_select.html)

onelinerhub: [How do I use SQLite xfilter to filter data?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-xfilter-to-filter-data)