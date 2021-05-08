# Extract audio from video

```bash
ffmpeg -i in.mp4 -vn -q:a 0 -map a out.mp3
```

- in.mp4 - input video file to extract audio from
- -vn - skip video (leave only audio)
- -q:a 0 - sets best possible audio quality
- -map a - tells ffmpeg to select audio stream
- out.mp3 - resulting audio file
