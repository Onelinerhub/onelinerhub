# Server config example

### Configuration file is usually located at `/etc/manticoresearch/manticore.conf`:

```bash
searchd {
  listen = 127.0.0.1:9312
  listen = 127.0.0.1:9306:mysql
  listen = 127.0.0.1:9308:http
  pid_file = /var/run/manticore/searchd.pid
  data_dir = /var/lib/manticore
}

indexer {
  mem_limit = 1G
}
```

- `listen` - list interfaces and protocols to enable
- `pid_file` - PID file path
- `data_dir` - path for a folder to store real time indexes data
- `searchd` - configure search server
- `indexer` - configure indexer tool
- `mem_limit` - limit indexing memory to the specified amount


