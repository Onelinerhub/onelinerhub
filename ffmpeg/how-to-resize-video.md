# How to resize video

```bash
ffmpeg -i in.mp4 -vf scale=320:240 out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - scale video
- `320` - scaling width
- `240` - scaling height
- `out.mp4` - resulting video file

group: resize


