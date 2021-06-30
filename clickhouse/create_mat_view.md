# Create AggregatingMergeTree materialized view

```sql
CREATE MATERIALIZED VIEW tbl_view (event String, val AggregateFunction(sum, Int64), date Date)
ENGINE = AggregatingMergeTree PARTITION BY toYYYYMMDD(date) ORDER BY (event)
AS SELECT event, sumState(val) AS val, toYYYYMMDD(ts) AS date FROM tbl GROUP BY event, date
```

- tbl_view - name of the view to create
- val AggregateFunction(sum, Int64) - this column will contain sum of original ```val``` column (see [tbl declaration](/clickhouse/create_merge_tree))
- AggregatingMergeTree - our materialized view will be of aggregating type
- PARTITION BY toYYYYMMDD(date) - data will be partitioned by day
- ORDER BY (event) - primary key
- AS SELECT - specify query to populate data on the fly
- sumState(val) AS val - special function to let clickhouse know we want resulting ```val``` column to have sum of original ```val``` columns

group: create
