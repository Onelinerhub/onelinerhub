# How to upscale video to 4k

```bash
ffmpeg -i in.mp4 -vf scale=-1:2160:flags=lanczos -c:v libx264 -crf 21 out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - scale video
- `-1` - width will be automatically calculated based on aspect ratio
- `2160` - set scaling height to 2160 pixels (4k resolution)
- `flags=lanczos` - use `lanczos` [scaling algorithm](https://ffmpeg.org/ffmpeg-scaler.html)
- `-c:v libx264` - use H.264 codec
- `-crf 21` - use good quality for encoding
- `out.mp4` - resulting video file

group: upscale


