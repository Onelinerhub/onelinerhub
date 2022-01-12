# Run official Clickhouse docker container

```docker
docker run -d -p 8123:8123 -p 9000:9000 yandex/clickhouse-server
```

- `run` - starts specified container
- `-d` - runs container as a background daemon
- `-p 8123:8123` - expose HTTP 8123 port to the same local port
- `-p 9000:9000` - expose Clickhouse 9000 port to the same local port
- `yandex/clickhouse-server` - name of the official Clickhouse docker image

## Example: 
```docker
docker run -d -p 8123:8123 -p 9000:9000 yandex/clickhouse-server
curl 127.0.0.1:8123
```
```
Ok.
```

