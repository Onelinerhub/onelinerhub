# How to limit memory for docker container

```docker
docker run -it -m 2g ubuntu
```

- `docker run` - launch docker container
- `-it` - immediately connect to container terminal after launch
- `-m` - amount of memory docker container will be allowed to use
- `2g` - use only 2 gigabytes of memory
- `ubuntu` - name of the image to run container from

group: resources

