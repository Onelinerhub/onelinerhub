# Get table size

```sql
SELECT formatReadableSize(sum(bytes)) FROM system.parts WHERE active AND table = 'tbl';
```

- `formatReadableSize` - converts bytes into human-readable form
- `sum(bytes)` - get sum of all parts sizes of our table
- `system.parts` - system table with table parts info
- `active` - select only active parts
- `table = 'tbl'` - name of the table to get size for (`tbl` in our case)

group: sizes

## Example: 
```sql
SELECT  formatReadableSize(sum(bytes)) as size FROM system.parts WHERE active AND table = 'tbl';
```
```
┌─size──────┐
│ 49.00 MiB │
└───────────┘

```

