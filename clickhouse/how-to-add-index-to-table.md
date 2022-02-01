# How to add index to table

```sql
ALTER TABLE tbl ADD INDEX col_index(col) TYPE minmax GRANULARITY 3
```

- `ALTER TABLE` - change specified table
- `tbl` - sample table to add index to
- `ADD INDEX` - adds [data skipping index](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#table_engine-mergetree-data_skipping-indexes)
- `col_index` - index name
- `col` - column to index (can have multiple columns, separated by `,`)
- `TYPE` - index type
- `minmax` - simple minmax index (the same type as primary key)
- `GRANULARITY` - how many granules to store for each table granule (3 in our case)

group: indexes


link_youtube: https://youtu.be/xjNcKOiZhZ8
