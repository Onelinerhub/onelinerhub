# How to remove all unused images, volumes and containers from Docker

```docker
docker system prune -a --volumes
```

- `system prune` - removes dangling images and stopped containers
- `-a` - remove all unused images, not only dangling
- `--volumes` - also remove unused volumes

