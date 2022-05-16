# How to resize video to 480p

```bash
ffmpeg -i in.mp4 -vf scale=-1:480 out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - scale video
- `-1` - width will be automatically calculated based on aspect ratio
- `480` - scaling height
- `out.mp4` - resulting video file

group: resize


