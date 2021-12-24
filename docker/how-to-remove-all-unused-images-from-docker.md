# How to remove all unused images from Docker

```docker
docker system prune -a
```

- `system prune` - removes dangling images and stopped containers
- `-a` - remove all unused images, not only dangling

