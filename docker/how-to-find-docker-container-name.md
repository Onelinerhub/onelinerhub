# How to find docker container name

### Container name is seen under the `NAMES` column of `docker ps` command:

```bash
docker ps -a
```

- `ps -a` - lists all docker containers

group: id

## Example: 
```bash
docker ps -a
```
```
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
03b975f84634   nginx     "/docker-entrypoint.…"   5 minutes ago    Exited (0) 4 minutes ago             eager_mirzakhani
```

link_youtube: https://youtu.be/xRqkXuXwg6M
