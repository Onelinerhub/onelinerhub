# SQL over HTTP usage example

```bash
curl -X POST localhost:9308/sql --data-urlencode "query=SELECT * FROM index1 WHERE MATCH('text')"
```

- `curl` - sends HTTP requests
- `-X POST` - send POST request
- `localhost` - Manticore search host
- `9308` - Manticore search port
- `/sql` - endpoint for HTTP SQL requests
- `--data-urlencode` - will encode data that we're going to send
- `query=` - SQL query to match something
- `index1` - name of the index
- `text` - sample text to match among our index


