# Atomic select and update (e.g. fetch unique rows on each request)

```sql
START TRANSACTION;
SELECT id FROM tbl WHERE processed = 0 LIMIT 1 FOR UPDATE;
UPDATE tbl SET processed = 1 WHERE id = 2;
COMMIT;
```

- START TRANSACTION - starts transaction
- tbl - table to select rows from
- processed = 0 - condition to select rows from table
- LIMIT 1 - select only one row
- FOR UPDATE - lock selected rows till they are updated by us
- SET processed = 1 - updated selected row (after possible processing)
- id = 2 - condition to update selected row (use fetched ID of a row)
- COMMIT - finish transaction (lock will be released after that)
