# How to change video resolution

```bash
ffmpeg -i in.mp4 -vf scale=100:200,setsar=1:1 out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `scale=` - change video resolution to specified size
- `100` - set width to `100` pixels
- `200` - set height to `200` pixels
- `setsar=1:1` - use simple pixel aspect ratio
- `out.mp4` - resulting video file

group: resolution


