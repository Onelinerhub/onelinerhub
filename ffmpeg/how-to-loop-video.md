# How to loop video

```bash
ffmpeg -stream_loop 3 -i in.mp4 -c copy out.mp4
```

- `-stream_loop` - loops specified input streams given amount of times
- `3` - repeat 3 times
- `-i in.mp4` - input video file to loop
- `-c copy` - do not encode/convert, only copy
- `out.mp4` - resulting video file


