# JSON over HTTP protocol example

```bash
curl -X POST localhost:9308/json/search -d '{"index":"index1","query":{"match_phrase":{"*":"Text"}}}'
```

- `curl` - sends HTTP requests
- `-X POST` - send POST request
- `localhost` - Manticore search host
- `9308` - Manticore search port
- `index1` - name of the index
- `match_phrase` - will match documents by specified rules
- `"*":"Text"` - will search for `Text` in all fields of index

group: http


