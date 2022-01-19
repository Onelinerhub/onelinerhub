# Add row number to results

```sql
SELECT rowNumberInAllBlocks(), * FROM tbl;
```

- `rowNumberInAllBlocks` - returns current row number
- `FROM tbl` - sample table to select data from

group: summary

## Example: 
```sql
SELECT rowNumberInAllBlocks(), * FROM tbl
```
```
┌─rowNumberInAllBlocks()─┬───────date─┬─col────┐
│                      0 │ 2022-01-07 │ Donald │
│                      1 │ 2022-01-10 │ Donald │
│                      2 │ 2022-01-11 │ Donald │
│                      3 │ 2022-01-11 │ Donald │
│                      4 │ 2022-01-12 │ Donald │
...
```

link_youtube: https://youtu.be/1h0F3yAoP9E
