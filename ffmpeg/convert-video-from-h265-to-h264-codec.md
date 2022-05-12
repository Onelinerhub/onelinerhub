# Convert video from H.265 to H.264 codec

```bash
ffmpeg -i in.mp4 -map 0 -c:v libx264 -crf 18 -vf format=yuv420p -c:a copy out.mkv

```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libx264` - use H.264 video codec
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `-vf format=yuv420p` - use `yuv420p` pixel format
- `-c:a copy` - copy audio without converting
- `out.mkv` - resulting video file

group: h265


