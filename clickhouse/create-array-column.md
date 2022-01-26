# Create array column

```sql
CREATE TABLE tbl3 (ts DateTime, list Array(String)) ENGINE = MergeTree ORDER BY (ts)
```

- `tbl3` - name of the table with array column to create
- `list` - name of the array column
- `Array(String)` - this will be array of strings

group: array


link_youtube: https://youtu.be/giEkNCEHCHY
