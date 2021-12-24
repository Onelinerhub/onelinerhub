# How to build docker image from Dockerfile

```docker
docker build -t some_name .
```

- `build` - builds an image from [Dockerfile](https://onelinerhub.com/docker/dockerfile-example) 
- `-t some_name` - assign name to the image
- `.` - path to the folder which [Dockerfile](https://onelinerhub.com/docker/dockerfile-example) is located in

group: build

## Example: 
```docker
docker build -t some_name .
docker run some_name
```
