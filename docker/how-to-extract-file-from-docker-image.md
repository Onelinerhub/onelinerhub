# How to extract file from docker image

### In order to extract file from docker image, we will create temporary container, copy the file and then delete container.

```docker
docker run --name=tmp ubuntu
docker cp tmp:/etc/passwd /tmp
docker rm tmp
```

- `docker run` - launch container
- `--name=tmp` - set it's name to `tmp`
- `ubuntu` - name of the image to create container from
- `docker cp` - copy file from container to local machine
- `tmp` - name of the container to copy from
- `/etc/passwd` - file which we need to extract
- `/tmp` - local path to copy file to
- `docker rm tmp` - remove `tmp` container

