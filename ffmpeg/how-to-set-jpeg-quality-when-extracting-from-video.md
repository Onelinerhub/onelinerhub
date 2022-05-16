# How to set JPEG quality when extracting from video

```bash
ffmpeg -i in.mp4 -q:v 2 out_%03d.jpg
```

- `-i in.mp4` - input video file
- `-q:v` - set resulting image quality
- `2` - use the best possible quality, use values from `2` (best) to `31` (worst)
- `out_%03d.jpg` - output image name template

group: video_thumbnail


