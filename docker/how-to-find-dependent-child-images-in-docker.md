# How to find dependent child images in docker

```docker
PARENT=ba6acccedd29; docker inspect --format='"{{.Id}}" : "{{.Parent}}"' $(docker images --filter "since=$PARENT" --quiet)  | grep $PARENT
```

- `PARENT=` - declare `PARENT` variable
- `ba6acccedd29` - id of the image to get child images for
- `docker inspect` - gets detailed information about an image
- `--format` - return formatted data
- `"{{.Id}}" : "{{.Parent}}"` - we will see `"child-id" : "parent-id"` lines
- `docker images` - list docker images
- `--filter` - filter images list
- `since=$PARENT` - show only those images which were created after parent image
- `grep $PARENT` - finally, filter output to see only children of the specified parent


link_youtube: https://youtu.be/Q6C8Bag9sow
