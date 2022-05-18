# How to set MPEG-4 video quality using "qscale" option

```bash
ffmpeg -i in.mp4 -c:v mpeg4 -q:v 10 out.avi
```

- `-i in.mp4` - input video file
- `-c:v mpeg4` - use `mpeg4` codec for video
- `-q:v` - set video quality level, from `1` (best) to `31` (worst)
- `10` - use average quality level


