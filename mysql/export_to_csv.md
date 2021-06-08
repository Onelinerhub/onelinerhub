# Export table or query into CSV

```sql
SELECT * INTO OUTFILE '/tmp/dump.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
FROM tablename WHERE id > 10;
```

- '/tmp/dump.csv' - path to the final file (directory should be writeable by mysql)
- FIELDS TERMINATED BY ',' - use ```,``` as a column separator
- ENCLOSED BY '"' - wrap column values into doublequotes
- LINES TERMINATED BY '\n' - line break
- tablename - name of the table to select data from
- WHERE id > 10 - example query condition, you can use any query here, including ```WHERE```, ```ORDER```, ```GROUP``` ...
