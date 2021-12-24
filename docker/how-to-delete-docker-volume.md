# How to delete docker volume

### Before volume removal make sure to remove all containers that volume is used for

```docker
docker volume rm data
```

- `volume` - manipulate volumes
- `rm` - remove specified volume
- `data` - name of the volume to remove

group: volume

