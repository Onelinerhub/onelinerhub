# How to change video resolution and keep aspect ratio

### In order to keep aspect ratio, set only one target dimension (width or height) and leave the other one as `-1`:

```bash
ffmpeg -i in.mp4 -vf scale=-1:180 out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - change video resolution to specified size
- `-1` - width will be calculated automatically based on aspect ratio
- `180` - set height to `180` pixels
- `out.mp4` - resulting video file

group: resolution


