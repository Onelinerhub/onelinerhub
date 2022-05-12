# Encoding video for usage on a website (H.264)

```bash
ffmpeg -i in.mov -vcodec libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mov` - input video file
- `-vcodec libx264` - use H.264 video codec
- `-pix_fmt yuv420p` - use yuv420p pixel format
- `-crf 18` - select bitrate for quality (`0` is best, `51` is worst), `18` is a good enough for most cases
- `-movflags +faststart` - adds metadata to the beginning of the file, so it can start playing before full download 
- `out.mp4` - resulting file

group: web


