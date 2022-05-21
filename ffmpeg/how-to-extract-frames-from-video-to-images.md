# How to extract frames from video to high quality images

```bash
ffmpeg -i in.mp4 -r 1/1 out-%03d.png
```

- `-i in.mp4` - input video file
- `-r` - set frame rate to extract frames at
- `1/1` - extract 1 frame every second
- `out-%03d.png` - output file name template (e.g. `out-001.png`, `out-002.png`,...)


link_youtube: https://youtu.be/XhBd04wPxiM
