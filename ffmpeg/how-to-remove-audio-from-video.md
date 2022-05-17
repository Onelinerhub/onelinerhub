# How to remove audio from video

```bash
ffmpeg -i in.mp4 -vcodec copy -an out.mp4
```

- `-i in.mp4` - input video file
- `-vcodec copy` - copy video instead of converting/encoding
- `-an` - removes audio channel from resulting file
- `out.mp4` - resulting video file


