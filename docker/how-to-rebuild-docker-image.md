# How to rebuild docker image

```docker
docker build --no-cache -t some_name .
```

- `build` - builds an image from [Dockerfile](https://onelinerhub.com/docker/dockerfile-example) 
- `-t some_name` - assign name to the image
- `.` - path to the folder which [Dockerfile](https://onelinerhub.com/docker/dockerfile-example) is located in
- ` --no-cache` - Docker will rebuild all components without cache

group: build

