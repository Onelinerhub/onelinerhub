# How to encode video using AV1 codec

```bash
ffmpeg -i in.mp4 -c:v libaom-av1 -crf 18 -b:v 0 out.mkv
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libaom-av1` - use `AV1` video codec
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `-b:v 0` - this should be used to set quality with `crf` flag
- `out.mkv` - resulting video file

group: av1


