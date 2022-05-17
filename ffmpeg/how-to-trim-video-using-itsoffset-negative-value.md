# How to trim video using itsoffset negative value

```bash
ffmpeg -itsoffset -5 -i in.mp4 out.mp4
```

- `-itsoffset` - delays input stream by specified number of seconds
- `-5` - input stream will be trimmed by 5 seconds from start
- `-i in.mp4` - input video file
- `out.mp4` - resulting video file

group: itsoffset


