# How do I create a hash index in PostgreSQL?
// plain

A hash index in PostgreSQL is created using the `CREATE INDEX` command. This is an example of creating a hash index on the `name` column of the `customers` table:

```sql
CREATE INDEX customers_name_hash_idx
  ON customers USING hash (name);
```

This command will create a hash index on the `name` column of the `customers` table. The index will use a hashing algorithm to store the data in an efficient manner, allowing for faster lookups and queries.

The parts of the command are:

1. `CREATE INDEX` - This is the command used to create the index.
2. `customers_name_hash_idx` - This is the name of the index.
3. `ON customers` - This specifies the table the index will be created on.
4. `USING hash` - This specifies the type of index to be created, in this case, a hash index.
5. `(name)` - This specifies the column the index will be created on.

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/indexes-types.html).

onelinerhub: [How do I create a hash index in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-hash-index-in-postgresql)