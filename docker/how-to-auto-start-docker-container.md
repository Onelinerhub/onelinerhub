# How to auto start docker container

```docker
docker run -d --restart unless-stopped my_image
```

- `run` - starts specified container
- `-d` - run container in background
- `--restart` - specify restart policy
- `unless-stopped` - will always [re]start this container unless it is manually stopped by us 
- `my_image` - image ID or name to run

group: run

