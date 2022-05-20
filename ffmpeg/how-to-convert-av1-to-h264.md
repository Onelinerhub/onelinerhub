# How to convert AV1 to H.264

```bash
ffmpeg -i in.mkv -c:v libx264 -crf 18 out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mkv` - input video file
- `-c:v libx264` - use [`H.264`](/ffmpeg/best-quality-for-h264-codec) video codec
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `out.mp4` - resulting video file

group: av1


link_youtube: https://youtu.be/EVe0ZV2VQG4
