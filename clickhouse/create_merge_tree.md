# Create MergeTree table

```sql
CREATE TABLE tbl (event String, ts DateTime, val Int64) ENGINE = MergeTree PARTITION BY toYYYYMMDD(ts) ORDER BY (event, ts);
```

- tbl - name of the table to create (e.g. table to store events)
- (event String, ts DateTime, val Int64 - columns declaration
- MergeTree - engine definition
- toYYYYMMDD(ts) - data will be partitioned by days (e.g. each day will represent it's own partition)
- ORDER BY (event, ts) - these columns pair will be used as primary key (thus, making read access faster when specifying them is select query)

group: create
