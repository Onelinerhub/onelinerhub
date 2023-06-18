# How do I generate a row number for each record in a SQLite database?
// plain

To generate a row number for each record in a SQLite database, you can use the [`row_number()`](https://www.sqlite.org/lang_corefunc.html#row_number) window function. This function assigns a sequential integer to each row in the result set.

For example, the following code block generates a row number for each record in the `customers` table:

```sql
SELECT
    row_number() OVER (ORDER BY customer_id) AS row_num,
    customer_id,
    first_name,
    last_name
FROM customers;
```

This code block returns the following output:

```
row_num  customer_id  first_name  last_name
1        1            John        Smith
2        2            Jane        Doe
3        3            Joe         Brown
```

The code consists of the following parts:

- `SELECT`: specifies the columns to be included in the result set
- `row_number() OVER (ORDER BY customer_id)`: generates a sequential integer for each row in the result set, ordered by the `customer_id` column
- `AS row_num`: assigns the name `row_num` to the generated row number
- `FROM customers`: specifies the table from which the data is to be retrieved

For more information, see the [SQLite documentation](https://www.sqlite.org/lang_corefunc.html#row_number).

onelinerhub: [How do I generate a row number for each record in a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-generate-a-row-number-for-each-record-in-a-sqlite-database)