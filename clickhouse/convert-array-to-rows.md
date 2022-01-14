# Convert array to rows

```sql
SELECT arrayJoin([1, 2, 3])
```

- `arrayJoin` - will expand array to rows (each row for each array element)
- `[1, 2, 3]` - sample array to convert to rows

group: array_to

## Example: 
```sql
SELECT arrayJoin([1, 2, 3]);
SELECT arrayJoin([1, 2, 3]), now();

```
```
┌─arrayJoin([1, 2, 3])─┐
│                    1 │
│                    2 │
│                    3 │
└──────────────────────┘

┌─arrayJoin([1, 2, 3])─┬───────────────now()─┐
│                    1 │ 2022-01-14 17:53:02 │
│                    2 │ 2022-01-14 17:53:02 │
│                    3 │ 2022-01-14 17:53:02 │
└──────────────────────┴─────────────────────┘
```

