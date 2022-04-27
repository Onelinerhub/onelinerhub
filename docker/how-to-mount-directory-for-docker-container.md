# How to mount directory for docker container

```docker
docker run -it -v /var/www:/www ubuntu
```

- `docker run` - launch docker container
- `-it` - connect to container right after launch
- `-v` - mount specified directories
- `/var/www` - directory on the local (docker host) machine to mount
- `/www` - path that mounted directory will be accessible from container
- `ubuntu` - name of the image to run container from


link_youtube: https://youtu.be/GU8UJR6oCyc
