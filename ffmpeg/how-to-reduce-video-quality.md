# How to reduce video quality

```bash
ffmpeg -i in.mp4 -crf 30 out.mp4
```

- `-i in.mp4` - input video file
- `-crf` - sets quality for each frame, from `0` (best) to `51` worst
- `30` - use worse quality for resulting video (try different values here)
- `out.mp4` - resulting video file

group: quality


