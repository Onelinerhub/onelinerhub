# How to set video quality using QP option

```bash
ffmpeg -i in.mp4 -qp 18 out.mp4
```

- `-i in.mp4` - input video file
- `-qp` - sets quality for each frame, from `0` (best) to `51` worst
- `18` - use quite good quality for resulting video
- `out.mp4` - resulting video file

group: quality


