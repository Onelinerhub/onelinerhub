# Insert data over HTTP

```bash
curl "127.0.0.1:8123?query=INSERT+INTO+tbl+FORMAT+TSV" --data-binary @data.tsv
```

- `curl` - use curl to send HTTP request
- `127.0.0.1` - Clickhouse host IP
- `8123` - Clickhouse server port
- `query` - insert query and format in url-encoded form
- `--data-binary` - will post given data
- `@data.tsv` - curl will post data from this TSV formatted file

group: http

## Example: 
```bash
curl "127.0.0.1:8123?query=select+now()"
```
```
2022-01-12 19:02:22
```

