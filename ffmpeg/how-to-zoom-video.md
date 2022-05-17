# How to zoom video

```bash
ffmpeg -i in.mp4 -vf "scale=2*iw:-1,crop=iw/2:ih/2" out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - scale video
- `2*iw:-1` - zoom in video twice (`2*iw` means double video width, `-1` to calculate height automatically)
- `crop=` - crop video
- `iw/2:ih/2` - half of original video size and height
- `out.mp4` - resulting video file

group: zoom


