# How to change video duration

### In order to change duration, you can either [change speed]() or cut video:

```bash
ffmpeg -i in.mp4 -ss 00:00:03 -t 00:00:05 out.mp4
```

- `-i in.mp4` - input video file
- `-ss` - set start time to start cutting at
- `00:00:03` - start cutting at 3 seconds from video start
- `-t` - total length of resulting video
- `00:00:05` - resulting video will be 5 seconds length
- `out.mp4` - resulting video file

group: duration


