# How do I use PostgreSQL arrays?
// plain

PostgreSQL arrays are data structures that allow you to store multiple elements of the same data type. They are useful for storing related data that can be queried and manipulated together.

To use PostgreSQL arrays, you must first declare an array column in a table. This is done by adding the `ARRAY` keyword to the column definition. For example:

```
CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  colors ARRAY
);
```

Once the array column is declared, you can insert data into it. This is done by providing a comma-separated list of elements within square brackets. For example:

```
INSERT INTO items (id, colors)
VALUES (1, ['red', 'green', 'blue']);
```

You can then select data from the array column by using the `ANY` operator. This operator returns true if any value in the array matches the specified condition. For example:

```
SELECT * FROM items
WHERE 'red' = ANY (colors);
```

The output of the above query would be the item with an `id` of 1.

You can also use array functions to manipulate the data stored in an array column. For example, the `array_length` function returns the length of an array column. For example:

```
SELECT array_length(colors, 1) FROM items;

## Output example

3
```

For more information about PostgreSQL arrays, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/arrays.html).

onelinerhub: [How do I use PostgreSQL arrays?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-arrays)