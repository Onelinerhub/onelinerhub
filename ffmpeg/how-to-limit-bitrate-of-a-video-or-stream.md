# How to limit bitrate of a video or stream

```bash
ffmpeg-i in.mp4 -c:v libx264 -b:v 2M -maxrate 2M -bufsize 1M out.mp4
```

- `-i in.mp4` - input video file
- `-c:v libx264` - use [H.264 codec](/ffmpeg/encoding-video-for-usage-on-a-website-h264)
- `-b:v 2M` - target average bitrate is 2Mbit/s
- `-maxrate 2M` - limits maximum bitrate to the specified value (`2M` in our case)
- `-bufsize 1M` - affects bitrate variation (lower size - lower variation), defines how often average bitrate is calculated (recommended value is somewhere near `-b:v` option value to start from)
- `out.mp4` - resulting video file


