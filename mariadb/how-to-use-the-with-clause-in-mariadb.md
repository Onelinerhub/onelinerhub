# How to use the WITH clause in Mariadb?
// plain

The WITH clause in Mariadb is used to define a temporary named result set, known as a Common Table Expression (CTE). It can be used to simplify complex queries by breaking them down into smaller, more manageable parts.

## Example

```
WITH cte_name AS (
  SELECT * FROM table_name
)
SELECT * FROM cte_name;
```

## Output example

```
+--------+--------+
| column | value  |
+--------+--------+
|   ...  |   ...  |
+--------+--------+
```

## Code explanation

- WITH cte_name AS: This defines the CTE and assigns it a name.
- SELECT * FROM table_name: This is the query that will be used to populate the CTE.
- SELECT * FROM cte_name: This is the query that will use the CTE.

## Helpful links
- https://mariadb.com/kb/en/library/with/
- https://www.tutorialspoint.com/mariadb/mariadb_with_clause.htm

onelinerhub: [How to use the WITH clause in Mariadb?](https://onelinerhub.com/mariadb/how-to-use-the-with-clause-in-mariadb)