# How to delete all docker containers

```bash
docker rm $(docker ps --filter status=exited -q)
```

- `rm` - removes specified containers
- `docker ps --filter status=exited -q` - returns a list of all stopped container IDs

group: delete


link_youtube: https://youtu.be/j87Zk_odwDA
