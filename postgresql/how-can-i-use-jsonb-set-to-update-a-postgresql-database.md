# How can I use jsonb_set to update a PostgreSQL database?
// plain

JSONB_SET is a PostgreSQL function used to update fields in a JSONB column. It allows for the insertion of new values, as well as the replacement of existing values.

## Example


```
UPDATE my_table
SET my_jsonb_column = jsonb_set(my_jsonb_column, '{name}', '"John"')
WHERE id = 1;
```

The above example will update the `my_jsonb_column` in `my_table` with the `id` of `1` and set the `name` field in the JSONB column to `John`.

## Code explanation


1. `UPDATE my_table` - This is used to indicate which table we are updating.
2. `SET my_jsonb_column = jsonb_set(my_jsonb_column, '{name}', '"John"')` - This is used to set the `my_jsonb_column` to the return value of `jsonb_set` with the `name` field and the value `John`.
3. `WHERE id = 1` - This is used to indicate which record we are updating.

## Helpful links

- [PostgreSQL Documentation: jsonb_set](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSONB-SET)

onelinerhub: [How can I use jsonb_set to update a PostgreSQL database?](https://onelinerhub.com/postgresql/how-can-i-use-jsonb-set-to-update-a-postgresql-database)