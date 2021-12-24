# How to get logs from docker container

```docker
docker logs --tail 2 0548543a2e98
```

- `docker logs` - get logs from specified container
- `--tail 2` - show only last 2 lines of logs
- `0548543a2e98` - ID of the container to get logs for

