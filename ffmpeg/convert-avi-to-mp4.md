# Convert avi to mp4

### Since `avi` and `mp4` are containers, not codecs, we simply copy video/audio streams:

```bash
ffmpeg -i in.avi -c:v copy -c:a copy out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.avi` - input video file
- `-c:v copy` - just copy video stream from input to output
- `-c:a copy` - just copy audio stream from input to output
- `out.mp4` - resulting file

group: avi


