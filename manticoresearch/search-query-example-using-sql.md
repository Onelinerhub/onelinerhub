# Search query example using Mysql protocol

```bash
mysql -H 127.0.0.1 -P 9306 --protocol tcp -e "SELECT * FROM index1 WHERE MATCH('text')"
```

- `mysql` - mysql client
- `-H` - specify Manticore search host IP
- `-P` - specify Manticore search server port
- `index1` - name of the index
- `text` - sample text to search for in index

group: mysql


