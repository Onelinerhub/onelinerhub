# Connect to Manticoresearch using Mysql client

```bash
mysql -H 127.0.0.1 -P 9306 --protocol tcp
```

- `mysql` - mysql client
- `-H` - specify Manticore search host IP
- `-P` - specify Manticore search server port
- `--protocol tcp` - ensure Mysql client will connect through TCP (not unix socket)

group: mysql


