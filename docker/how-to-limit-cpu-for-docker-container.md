# How to limit CPU for docker container

```docker
docker run -it --cpus="2.0" ubuntu
```

- `docker run` - launch docker container
- `-it` - immediately connect to container terminal after launch
- `--cpus` - specify amount of CPUs docker container will be allowed to use
- `2.0` - use only 2 CPUs
- `ubuntu` - name of the image to run container from

group: resources

