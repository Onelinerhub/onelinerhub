# How to stop all running docker containers

```bash
docker container stop $(docker ps -q)
```

- `docker container` - manipulate containers
- `stop` - stops specified containers
- `$(docker ps -q)` - will list all running containers

group: stop

## Example: 
```bash
docker container stop $(docker ps -q)
```
```
3bd2bf8272b7
6c303abafe66
704b7deb0fd7
```
