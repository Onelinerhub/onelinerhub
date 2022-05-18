# How to deinterlace video

```bash
ffmpeg -i in.vob -vf yadif -c:v libx264 -crf 18 out.mp4
```

- `-i in.vob` - input video to deinterlace
- `-vf` - apply specific video filters
- `yadif` - this will deinterlace video
- `-c:v libx264` - use [H.264 codec](/ffmpeg/using-crf-with-h264-codec)
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `out.mp4` - resulting video file


