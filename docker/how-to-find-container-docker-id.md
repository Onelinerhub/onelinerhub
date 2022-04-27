# How to find docker container id

### Container ID is seen under the first column of `docker ps` command:

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

link_youtube: https://youtu.be/ElsU1QfYtfw
