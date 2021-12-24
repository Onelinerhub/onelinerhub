# How to find container docker id

### Container ID is seen under the first column of `docker ps` command:

```bash
docker ps -a
```

- `ps -a` - lists all docker containers

## Example: 
```bash
docker ps -a
```
```
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
03b975f84634   nginx     "/docker-entrypoint.…"   5 minutes ago    Exited (0) 4 minutes ago             eager_mirzakhani
```
