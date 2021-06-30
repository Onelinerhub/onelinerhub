# List table partitions

```sql
SELECT * FROM system.parts WHERE table = 'tbl' AND database = 'default';
```

- system.parts - system table with partitions meta data
- tbl - name of the table to get partitions for
- default - database where ```tbl``` resides

group: partitions
