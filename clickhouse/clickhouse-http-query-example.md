# Clickhouse HTTP query example

```bash
curl "127.0.0.1:8123" --data "SELECT * FROM tbl"
```

- `curl` - use curl to send HTTP request
- `127.0.0.1` - Clickhouse host IP
- `8123` - Clickhouse server port
- `--data` - send raw data to server
- `SELECT * FROM tbl` - sample request to execute on Clickhouse server

group: http

## Example: 
```bash
curl "127.0.0.1:8123" --data "SELECT * FROM tbl"
```
```
1970-01-01	Donald	0	125
2022-01-07	Donald	0	0
2022-01-10	Donald	0	0
...
```

link_youtube: https://youtu.be/dqs6JLK_e9E
