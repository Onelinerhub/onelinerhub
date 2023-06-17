# How can I create a hierarchical query in PostgreSQL?
// plain

A hierarchical query in PostgreSQL can be created using the `WITH RECURSIVE` statement. This statement allows for a recursive query that can traverse a tree-like structure. An example of a hierarchical query is shown below:

```
WITH RECURSIVE tree AS (
    SELECT id, parent_id, name
    FROM categories
    WHERE parent_id IS NULL
    UNION
    SELECT c.id, c.parent_id, c.name
    FROM categories c
    JOIN tree ON tree.id = c.parent_id
)
SELECT * FROM tree;
```

This query will output a table with the following columns:

- `id`: the category id
- `parent_id`: the parent category id
- `name`: the category name

The output of this query will be a list of categories and their parent categories, forming a hierarchy.

## Code explanation
**

- `WITH RECURSIVE tree AS (`: This statement indicates that a recursive query is being used.
- `SELECT id, parent_id, name`: This statement selects the columns from the `categories` table that will be used in the query.
- `WHERE parent_id IS NULL`: This statement specifies that only the top-level categories should be selected.
- `UNION`: This statement combines the results of two separate queries into one result set.
- `JOIN tree ON tree.id = c.parent_id`: This statement joins the `categories` table with the `tree` table on the `id` and `parent_id` columns.
- `SELECT * FROM tree`: This statement selects all the columns from the `tree` table.

**## Helpful links**

- [PostgreSQL Documentation: WITH](https://www.postgresql.org/docs/current/queries-with.html)
- [PostgreSQL Documentation: Recursive Queries](https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-RECURSIVE)

onelinerhub: [How can I create a hierarchical query in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-create-a-hierarchical-query-in-postgresql)