# How to delay video using itsoffset option

```bash
ffmpeg -itsoffset 5 -i in.mp4 out.mp4
```

- `-itsoffset` - delays input stream by specified number of seconds
- `5` - input stream will be delayed during 5 seconds
- `-i in.mp4` - input video file
- `out.mp4` - resulting video file

group: itsoffset


