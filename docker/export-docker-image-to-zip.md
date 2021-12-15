# Export docker image to zip

```docker
docker save efc62499a2e3 | gzip > image.tar.gz
```

- `efc62499a2e3` - image id to export 
- `gzip` - gzip output
- `image.tar.gz` - archive name to export image to

