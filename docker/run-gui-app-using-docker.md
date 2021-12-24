# Run GUI app using docker

```docker
docker run -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix jlesage/firefox
```

- `docker run` - launches specified image
- `-e` - passes environment variable
- `DISPLAY` - set `DISPLAY` variable
- `unix$DISPLAY` - pass current display value (usually `:0`) and `unix` to ensure we connect using unix socket
- `-v` - mount directory into the container
- `/tmp/.X11-unix:/tmp/.X11-unix` - share our X-server with container 
- `jlesage/firefox` - example GUI image (Firefox browser)

