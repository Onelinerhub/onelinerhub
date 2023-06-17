# How can I create a unique constraint in PostgreSQL?
// plain

To create a unique constraint in PostgreSQL, the following steps need to be taken:

1. Create a table with the desired fields.

```
CREATE TABLE table_name (
    field1 data_type,
    field2 data_type,
    ...
    fieldN data_type
);
```

2. Add a unique constraint to the table. This is done using the `UNIQUE` keyword.

```
ALTER TABLE table_name
ADD CONSTRAINT constraint_name UNIQUE (field1, field2, ..., fieldN);
```

3. Check the table's constraints using the `\d` command.

```
\d table_name
```

## Output example

```
                                   Table "public.table_name"
    Column     |           Type           | Collation | Nullable | Default
---------------+--------------------------+-----------+----------+---------
 field1        | character varying(100)   |           |          |
 field2        | integer                  |           |          |
 ...
 fieldN        | character varying(100)   |           |          |
Indexes:
    "constraint_name" UNIQUE CONSTRAINT, btree (field1, field2, ..., fieldN)
```

4. To delete a unique constraint, use the `DROP CONSTRAINT` command.

```
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
```

5. To rename a unique constraint, use the `RENAME CONSTRAINT` command.

```
ALTER TABLE table_name
RENAME CONSTRAINT old_constraint_name TO new_constraint_name;
```

6. To disable a unique constraint, use the `SET CONSTRAINT` command.

```
ALTER TABLE table_name
SET CONSTRAINT constraint_name DEFERRED;
```

7. To enable a unique constraint, use the `SET CONSTRAINT` command.

```
ALTER TABLE table_name
SET CONSTRAINT constraint_name IMMEDIATE;
```

## Helpful links
- [PostgreSQL Documentation - Unique Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-UNIQUE)
- [PostgreSQL Documentation - ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)

onelinerhub: [How can I create a unique constraint in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-create-a-unique-constraint-in-postgresql)