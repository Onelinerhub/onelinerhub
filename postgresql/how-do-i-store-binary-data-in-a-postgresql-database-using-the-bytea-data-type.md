# How do I store binary data in a Postgresql database using the bytea data type?
// plain

The `bytea` data type is a binary data type in Postgresql which allows for the storage of binary data. To store binary data using the `bytea` data type, the binary data must first be converted into a hexadecimal representation of the data. This can be done with the `encode` function.

For example:
```
SELECT encode(E'\xDEADBEEF', 'hex');
```

This will output `"DEADBEEF"` which is the hexadecimal representation of the binary data `\xDEADBEEF`.

Once the data is in hexadecimal representation, it can be inserted into a `bytea` column like so:
```
INSERT INTO mytable (mybyteacolumn) VALUES (decode('DEADBEEF', 'hex'));
```

This will insert the binary data `\xDEADBEEF` into the `mybyteacolumn` column of the `mytable` table.

To retrieve the binary data, the `encode` function can be used again:
```
SELECT encode(mybyteacolumn, 'hex') FROM mytable;
```

This will output the hexadecimal representation of the binary data stored in the `mybyteacolumn` column.

## Helpful links
- https://www.postgresql.org/docs/9.4/datatype-binary.html
- https://www.postgresql.org/docs/9.4/functions-string.html

onelinerhub: [How do I store binary data in a Postgresql database using the bytea data type?](https://onelinerhub.com/postgresql/how-do-i-store-binary-data-in-a-postgresql-database-using-the-bytea-data-type)