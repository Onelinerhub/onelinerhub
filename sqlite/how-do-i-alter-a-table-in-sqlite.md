# How do I alter a table in SQLite?
// plain

To alter a table in SQLite, you use the `ALTER TABLE` statement. This statement allows you to add, remove, or modify columns in an existing table.

For example, to add a new column named `date_created` to the `customers` table, you use the following statement:

```sql
ALTER TABLE customers
ADD COLUMN date_created DATE;
```

This statement adds a new column named `date_created` to the `customers` table. The column is of type `DATE`, which stores date and time values.

You can also use the `ALTER TABLE` statement to modify the data type of an existing column, rename an existing column, or drop an existing column.

For example, to modify the data type of the `date_created` column to `TEXT`, you use the following statement:

```sql
ALTER TABLE customers
MODIFY COLUMN date_created TEXT;
```

To rename the `date_created` column to `created_at`, you use the following statement:

```sql
ALTER TABLE customers
RENAME COLUMN date_created TO created_at;
```

To drop the `created_at` column, you use the following statement:

```sql
ALTER TABLE customers
DROP COLUMN created_at;
```

More information about the `ALTER TABLE` statement can be found in the [SQLite documentation](https://www.sqlite.org/lang_altertable.html).

onelinerhub: [How do I alter a table in SQLite?](https://onelinerhub.com/sqlite/how-do-i-alter-a-table-in-sqlite)