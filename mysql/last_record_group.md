# Select last record from group

```sql
WITH ranked AS (
  SELECT m.*, ROW_NUMBER() OVER (PARTITION BY name ORDER BY id DESC) AS rn
  FROM table m
)
SELECT * FROM ranked WHERE rn = 1
```

- WITH ranked AS - define ```ranked``` window ([mysql 8+](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html))
- ROW_NUMBER() - returns row number inside defined partition
- PARTITION BY name - partition window from ```table``` by ```name``` column (e.g. group by name)
- ORDER BY id DESC - order window by id (newest rows will come first)
- SELECT * FROM ranked - now select data from ```ranked``` table
- WHERE rn = 1 - make sure we select only last (newest) row for each group

group: record_order
