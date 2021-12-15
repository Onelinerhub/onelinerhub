# How to delete all docker images

```docker
docker rmi $(docker images -aq)
```

- `rmi` - removes specified images
- `docker images -aq` - removes list of all images IDs

group: delete

