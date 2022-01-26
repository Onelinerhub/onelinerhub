# Create table example

```sql
CREATE TABLE tbl (date Date, col String) ENGINE = MergeTree ORDER BY date;
```

- `CREATE TABLE` - creates specified table
- `tbl` - name of the table
- `date Date, col String` - columns declaration
- `ENGINE = MergeTree` - use MergeTree (most powerful Clickhouse engine)
- `ORDER BY date` - this is something similar to default index of the table (data will be stored in a specified sort order)

group: create


link_youtube: https://youtu.be/MIF3_X_rhJg
