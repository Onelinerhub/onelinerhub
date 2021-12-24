# How to add volume to docker container

```docker
docker volume create data
docker run -it --mount source=data,destination=/data ubuntu
```

- `docker volume` - volume manipulations
- `create` - create new volume
- `data` - name of the volume to be created
- `docker run` - launch container from specified image
- `-it` - connect to container command line when launched
- `--mount` - mount specified volume
- `source=data` - name of the volume to mount
- `destination=/data` - path which volume will be accessed from the container
- `ubuntu` - image name to launch

group: volume

## Example: 
```docker
# docker volume create data
# docker run -it --mount source=data,destination=/data ubuntu
root@b52eb21cff1d:/# ls -la /data/

```
```
drwxr-xr-x 2 root root 4096 Dec 24 10:29 .
drwxr-xr-x 1 root root 4096 Dec 24 10:32 ..
-rw-r--r-- 1 root root    0 Dec 24 10:29 hello.txt
```
