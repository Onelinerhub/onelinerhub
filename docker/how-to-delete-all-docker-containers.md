# How to delete all docker containers

```docker
docker rm $(docker ps --filter status=exited -q)
```

- `rm` - removes specified containers
- `docker ps --filter status=exited -q` - returns a list of all stopped container IDs

