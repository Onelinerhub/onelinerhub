# How to set video codec using vcodec option

```bash
ffmpeg -i in.mp4 -vcodec libx265 out.mp4
```

- `-i in.mp4` - input video file
- `-vcodec` - set custom video codec for encoding
- `libx265` - use [H.265 codec](/ffmpeg/encode-video-using-h265-codec) in this example

group: codecs_formats


