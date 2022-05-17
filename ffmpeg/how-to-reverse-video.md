# How to reverse video

```bash
ffmpeg -i in.mp4 -vf reverse out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `reverse` - filter used to reverse video
- `out.mp4` - resulting video file


