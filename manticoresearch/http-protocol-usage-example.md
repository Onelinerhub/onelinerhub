# HTTP protocol usage example

```manticoresearch
curl -X POST localhost:9308/sql --data-urlencode "query=SELECT * FROM index1 WHERE MATCH('text')"
```

- `curl` - sends HTTP requests
- `-X POST` - send POST request
- `localhost` - Manticoresearch host


