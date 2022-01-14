# Using ARRAY JOIN in queries

```sql
SELECT ts, list FROM tbl3 ARRAY JOIN list
```

- `ts` - datetime column
- `list` - name of the array column to expand
- `tbl3` - table with [array column in it](/clickhouse/create-array-column)
- `ARRAY JOIN` - will duplicate each row for each element of array and return resulting flat table

## Example: 
```sql
SELECT * FROM tbl3;
SELECT ts, list FROM tbl3 ARRAY JOIN list
```
```
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:32 │ ['a','b','c'] │
│ 2022-01-14 17:41:38 │ ['b','c','d'] │
└─────────────────────┴───────────────┘

┌──────────────────ts─┬─list─┐
│ 2022-01-14 17:41:32 │ a    │
│ 2022-01-14 17:41:32 │ b    │
│ 2022-01-14 17:41:32 │ c    │
│ 2022-01-14 17:41:38 │ b    │
│ 2022-01-14 17:41:38 │ c    │
│ 2022-01-14 17:41:38 │ d    │
└─────────────────────┴──────┘
```

