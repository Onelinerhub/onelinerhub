# How to covert TS video stream to MP4

```bash
ffmpeg -i in.ts -c:v libx264 -c:a aac out.mp4
```

- `-i in.ts` - input video file
- `-c:v libx264` - use H.264 codec
- `-c:a aac` - use [`AAC` codec](/ffmpeg/encode-mp3-to-aac) for audio
- `out.mp4` - resulting video file


