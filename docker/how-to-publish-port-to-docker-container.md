# How to publish port to docker container

```docker
docker run -it -p 81:80 nginx
```

- `docker run` - launch docker container
- `-it` - connect to container CLI right after launch
- `-p` - publish specified ports
- `81` - port of local machine (docker host)
- `80` - port of container to forward to specified local machine port
- `nginx` - name of the image to launch container from


## Additional keywords
- expose
- forward
- open
