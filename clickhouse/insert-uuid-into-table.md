# INSERT UUID into table

```sql
INSERT INTO utbl SELECT generateUUIDv4(), today(), 'Joe'
```

- `utbl` - name of the [table with UUID column](/clickhouse/create-table-with-uuid-column)
- `generateUUIDv4` - generates UUID value
- `today()` - sample value for `date` column
- `'Joe'` - sample value for `col` column

group: uuid

## Example: 
```sql
INSERT INTO utbl SELECT generateUUIDv4(), today(), 'Joe';
SELECT * FROM utbl;
```
```
┌─id───────────────────────────────────┬───────date─┬─col─┐
│ 4b06cbf8-96cc-4d85-8cfc-5cb905bf45d0 │ 2022-01-12 │ Joe │
└──────────────────────────────────────┴────────────┴─────┘
```

