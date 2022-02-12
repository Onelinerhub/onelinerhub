# How to access machine localhost from docker image

```docker
docker run -d --network="host" my_image
```

- `run` - launch container from specified image
- `-d` - starts container in background
- `--network="host"` - you'll be able to connect to machine localhost from container, just go to `127.0.0.1` on container
- `my_image` - name or ID of the image to launch


link_youtube: https://youtu.be/Zbj53WX2sso
