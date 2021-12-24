# How to pass environment variable to docker container

```docker
docker run -d -e SOME_VAR='some_val' image_name
```

- `docker run` - run specified image
- `-d` - run container in background
- `-e` - pass specified environment variable (can be used several times)
- `SOME_VAR` - environment variable name
- `some_val` - environment variable value
- `image_name` - name of the docker image to start


## Additional keywords
- set
- add
