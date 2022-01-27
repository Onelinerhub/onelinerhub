# Create table with UUID column

```sql
CREATE TABLE utbl ( id UUID, date Date, col String ) ENGINE = MergeTree ORDER BY date
```

- `utbl` - name of the table to create
- `id` - column name
- `UUID` - set `UUID` type for `id` column
- `date Date, col String` - other columns declaration
- `ENGINE = MergeTree ORDER BY date` - engine and sort order

group: uuid


link_youtube: https://youtu.be/rcv-zTLArhc
