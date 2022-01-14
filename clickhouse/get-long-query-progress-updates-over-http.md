# Get long query progress updates over HTTP

```sql
curl -i "127.0.0.1:8123?send_progress_in_http_headers=1" --data "SELECT * FROM large_table WHERE something = 1"
```

- `127.0.0.1:8123` - Clickhouse HTTP host/port to send query to
- `send_progress_in_http_headers` - will enable progress headers for this query (will send us `X-ClickHouse-Progress` headers periodically to update query status)
- `--data` - send query using POST
- `SELECT * FROM large_table` - assume this query will take long enough to see its progress
- `curl -i` - curl will show headers while executing request

## Example: 
```sql
curl -i "127.0.0.1:8123?send_progress_in_http_headers=1" --data "SELECT * FROM large_table WHERE something = 1"
```
```
HTTP/1.1 200 OK
...
X-ClickHouse-Progress: {"read_rows":"137363115","read_bytes":"549452460","written_rows":"0","written_bytes":"0","total_rows_to_read":"1222011084"}
X-ClickHouse-Progress: {"read_rows":"347774759","read_bytes":"1391099036","written_rows":"0","written_bytes":"0","total_rows_to_read":"1222011084"}
X-ClickHouse-Progress: {"read_rows":"559650718","read_bytes":"2238602872","written_rows":"0","written_bytes":"0","total_rows_to_read":"1222011084"}
X-ClickHouse-Progress: {"read_rows":"734606097","read_bytes":"2938424388","written_rows":"0","written_bytes":"0","total_rows_to_read":"1222011084"}
X-ClickHouse-Summary: {"read_rows":"838824690","read_bytes":"3355298760","written_rows":"0","written_bytes":"0","total_rows_to_read":"1222011084"}

431676695
261297029
457335217
54160200
292550297
54160200
```

