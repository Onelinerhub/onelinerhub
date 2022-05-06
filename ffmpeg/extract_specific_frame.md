# Create thumbnail from a specific video frame

```bash
ffmpeg -accurate_seek -ss 00:04:50 -i in.mp4 -frames:v 1 out.jpg
```

- `-i in.mp4` - input video file
- `-accurate_seek -ss 00:04:50` - select time of a frame to extract
- `-frames:v 1` - amount of frames to extract
- `out.jpg` - resulting image

group: video_thumbnail


link_youtube: https://youtu.be/wJiJZcukGo0
