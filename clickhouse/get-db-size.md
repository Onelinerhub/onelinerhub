# Get total database size

```sql
SELECT formatReadableSize(sum(bytes)) FROM system.parts WHERE active AND database = 'default';
```

- `formatReadableSize` - converts bytes into human-readable form
- `sum(bytes)` - get sum of all parts sizes of our table
- `system.parts` - system table with table parts info
- `active` - select only active parts
- `default` - name of the database to get size for (`tbl` in our case)

group: sizes

## Example: 
```sql
SELECT  formatReadableSize(sum(bytes)) as size FROM system.parts WHERE active AND table = 'tbl';
```
```
┌─size──────┐
│ 89.00 MiB │
└───────────┘

```

