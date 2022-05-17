# How to change video pixel format

```bash
ffmpeg -i in.mp4 -pix_fmt yuv420p out.mp4
```

- `-i in.mp4` - input video file
- `-pix_fmt yuv420p` - use yuv420p pixel format
- `out.mp4` - resulting video file

group: pix_fmt


