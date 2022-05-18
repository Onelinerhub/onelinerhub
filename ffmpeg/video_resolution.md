# Get video resolution

```bash
ffprobe -v quiet -print_format json -show_streams in.mp4 | egrep "(width|height)" | grep -v coded
```

- `in.mp4` - video to get resolution for
- `-print_format json -show_streams` - prints JSON media info
- `egrep "(width|height)"` - trims only width/height data from output
- `grep -v coded` - excludes unneeded info from output

group: resolution


link_youtube: https://youtu.be/_E74-uYS5Iw
