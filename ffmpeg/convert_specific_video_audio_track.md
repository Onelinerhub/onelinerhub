# Select specific video/audio track when converting video

```bash
ffmpeg -i input.mkv -map 0:v:0 -map 0:a:1 output.mp4
```

- `input.mkv` - input video file
- `-map 0:v:0` - will select first video track (indexes starting at 0)
- `-map 0:a:1` - will select second audio track (indexes starting at 0)
- `output.mp4` - output resulting video file


link_youtube: https://youtu.be/xiOBF4x625o
