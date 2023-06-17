# How do I store an array in a PostgreSQL database?
// plain

PostgreSQL can store arrays of data in a single column. This is done by using the `ARRAY` data type when creating a table. To create a table with an array column, the syntax looks like this:

```sql
CREATE TABLE my_table (
  id INTEGER PRIMARY KEY,
  my_array ARRAY
);
```

To insert an array into the table, you can use the `ARRAY` constructor. This takes a set of values and creates an array out of them. For example, to insert the array `[1, 2, 3]` into the table, the syntax would be:

```sql
INSERT INTO my_table (my_array) VALUES (ARRAY[1, 2, 3]);
```

To retrieve the array from the table, you can use the `ARRAY[]` operator. This will return the array stored in the column. For example, to get the array inserted above:

```sql
SELECT my_array FROM my_table;

-- Output: [1,2,3]
```

The `ARRAY` data type also allows you to store multidimensional arrays. This is done by nesting the `ARRAY` constructor. For example, to insert a two dimensional array `[[1, 2], [3, 4]]` into the table, the syntax would be:

```sql
INSERT INTO my_table (my_array) VALUES (ARRAY[ARRAY[1, 2], ARRAY[3, 4]]);
```

To get the two dimensional array back from the table:

```sql
SELECT my_array FROM my_table;

-- Output: [[1,2],[3,4]]
```

## Helpful links

- [PostgreSQL Documentation - Arrays](https://www.postgresql.org/docs/current/arrays.html)
- [PostgreSQL Documentation - Data Types](https://www.postgresql.org/docs/current/datatype.html)

onelinerhub: [How do I store an array in a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-store-an-array-in-a-postgresql-database)