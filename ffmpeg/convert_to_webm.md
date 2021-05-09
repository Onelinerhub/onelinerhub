# Convert video to WEBM

```bash
ffmpeg -i in.mp4 -b:v 1M out.webm
```

- in.mp4 - input video to convert
- -b:v 1M - set good quality (bitrate, bigger number = better quality)
- out.webm - resulting video file in WEBM format

group: convert_video
