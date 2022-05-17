# How to set video frame rate using CRF option

```bash
ffmpeg -i in.mp4 -crf 18 out.mp4
```

- `-i in.mp4` - input video file
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `out.mp4` - resulting video file


